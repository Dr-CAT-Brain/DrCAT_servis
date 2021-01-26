import os
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.decorators import method_decorator
from django.views import generic

from neuronet.Models import predict_picture
from .filters import TreatmentFilter
from .LabelDecoder import decode_label_detail
from neuronet.KNN import KNN
from neuronet.recomendation import get_hunt_hess_by_treatment, adapt_int_to_patology, get_recommendations

from .forms import TreatmentForm
from .models import Patient, Treatment, Doctor, FAQ, FAQItem, ClassificationType

LOGIN_URL = 'login'


@login_required(login_url=LOGIN_URL)
def cabinet_view(request):
    if request.method == "POST":
        form = PersonalData(request.POST, request.FILES)
        if form.is_valid():
            doctor = request.user.doctor
            doctor.full_name = form.cleaned_data['full_name']
            doctor.qualification = form.cleaned_data['qualification']
            doctor.experience = form.cleaned_data['experience']
            doctor.work_place = form.cleaned_data['work_place']
            doctor.education = form.cleaned_data['education']
            doctor.contacts = form.cleaned_data['contacts']
            if form.cleaned_data['image']:
                doctor.photo = form.cleaned_data['image']
            doctor.save()

    doctor = request.user.doctor
    data = {
        'full_name': doctor.full_name,
        'qualification': doctor.qualification,
        'work_place': doctor.work_place,
        'education': doctor.education,
        'experience': doctor.experience,
        'contacts': doctor.contacts,
        'photo': doctor.photo,
    }
    form = PersonalData(data)

    def get_queryset():
        search_query = request.GET.get('q')
        search_query = search_query if search_query else ''
        return Treatment.objects.filter(
            Q(doctor=doctor) & Q(patient__full_name__icontains=search_query)
        ).all()

    return render(request, 'cabinet.html',
                  context={'header': 'Личный кабинет',
                           'doctor': request.user.doctor,
                           'form': form,
                           'history': get_queryset,
                           })


class DoctorProfileDetailView(LoginRequiredMixin, generic.DetailView):
    model = Doctor
    template_name = "doctor_profile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        search_query = self.request.GET.get('q')
        search_query = search_query if search_query else ''

        pk = self.kwargs['pk']
        doctor = Doctor.objects.filter(id=pk).first()

        context['history'] = Treatment.objects.filter(
            Q(doctor=doctor) & Q(patient__full_name__icontains=search_query)
        ).all()

        return context


def get_absolute_path_to_project():
    return os.path.dirname(os.path.abspath(__file__)).replace('\\web', '').replace('\\', '/')


def treatment_form_view(request):
    if request.method == 'POST':
        form = TreatmentForm(request.POST, request.FILES)

        if form.is_valid():
            patient = Patient()
            treatment = Treatment()

            patient.full_name = form.cleaned_data['full_name']
            patient.age = form.cleaned_data['age']
            patient.save()

            treatment.time_passed = form.cleaned_data['time_passed']
            treatment.hematoma_volume = form.cleaned_data['hematoma_volume']

            treatment.is_injury = form.cleaned_data['is_injure']
            treatment.has_stroke_symptoms = form.cleaned_data['has_stroke_symptoms']

            treatment.neurological_deficit = form.cleaned_data['neurological_deficit']
            treatment.conscious_level = form.cleaned_data['conscious_level']

            print(form.cleaned_data['neurological_deficit'],
                  form.cleaned_data['conscious_level']
                  )

            treatment.snapshot = form.clean_snapshot()
            treatment.patient = patient

            if request.user.is_authenticated:
                treatment.doctor = request.user.doctor
            treatment.save()

            for diagnosis in form.cleaned_data['diagnoses'].iterator():
                patient.diagnoses.add(diagnosis)

            for contraindications in form.cleaned_data['temporary_contraindications'].iterator():
                treatment.temporary_contraindications.add(contraindications)

            treatment.save()
            patient.save()

            image_absolute_path = get_absolute_path_to_project() + treatment.snapshot.url

            prediction = predict_picture(image_absolute_path)

            patologies = []
            for i in ClassificationType.objects.filter(prediction=prediction).all():
                patologies.append(adapt_int_to_patology(i.value, treatment))

            prediction.recommend_text = get_recommendations(patologies)
            prediction.save()

            treatment.predict = prediction
            treatment.save()

            return HttpResponseRedirect(f'report/{treatment.id}')
    else:
        form = TreatmentForm()

    return render(request, 'treatment_form.html', {'form': form})


class TreatmentListView(LoginRequiredMixin, generic.ListView):
    # paginate_by = 10
    login_url = LOGIN_URL
    model = Treatment
    template_name = 'treatment_list.html'

    def get_ordering(self):
        ordering = self.request.GET.get('ordering', 'hematoma_volume')
        return ordering

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = TreatmentFilter(self.request.GET, queryset=Treatment.objects.all())
        context['header'] = 'Библиотека снимков'
        return context


@method_decorator(login_required, name='dispatch')
class TreatmentHistoryView(generic.ListView):
    model = Treatment
    template_name = 'treatment_list.html'

    def get_queryset(self):
        return Treatment.objects.filter(doctor=self.request.user.doctor).all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = TreatmentFilter(self.request.GET, queryset=self.get_queryset())
        context['header'] = 'История'
        return context


class TreatmentDetailView(generic.DetailView):
    model = Treatment
    template_name = "treatment_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs['pk']
        treatment = Treatment.objects.filter(id=pk).first()

        bool_to_str = {
            True: 'Да',
            False: 'Нет',
            None: 'Неизвестно'
        }

        neurological_deficit_to_str = {
            1: 'Лёгкая головная боль',
            2: 'Парезы ЧМН',
            3: 'Легкий очаговый дефицит',
            4: 'Выраженный очаговый дефицит',
        }

        conscious_level_to_str = {
            15: 'Ясное',
            14: 'Умеренное оглушение',
            12: 'Глубокое оглушение',
            9: 'Сопор',
            7: 'Умеренная кома',
            5: 'Глубокая кома',
            3: 'Терминальная кома',
        }

        context['is_injure_label'] = bool_to_str[treatment.is_injury]
        context['has_stroke_symptoms'] = bool_to_str[treatment.has_stroke_symptoms]
        context['neurological_deficit'] = neurological_deficit_to_str[treatment.neurological_deficit]
        context['conscious_level'] = conscious_level_to_str[treatment.conscious_level]
        context['predicted_diagnosis'] = decode_label_detail(ClassificationType.objects.filter(prediction=treatment.predict).all())
        context['hunt_hess'] = get_hunt_hess_by_treatment(treatment)
        context['similar_treatments'] = get_similar_snapshots(treatment, 3)

        return context


def get_similar_snapshots(treatment: Treatment, num=3) -> list:
    file_name = 'knn_model_save'
    knn = KNN()

    try:
        knn.load_form_file(get_absolute_path_to_project() + '/neuronet/' + file_name)
    except FileNotFoundError:
        knn = fit_knn_by_all_treatments(file_name)

    knn_set = knn.predict(treatment, num)
    return list(knn_set)


def fit_knn_by_all_treatments(file_name) -> KNN:
    knn = KNN()
    knn.fit(Treatment.objects.all())
    knn.save_model(get_absolute_path_to_project() + '/neuronet/' + file_name)
    return knn


def api_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('pwd')
        stay_logged_in = request.POST.get('stayloggedIn')

        if stay_logged_in != "true":
            request.session.set_expiry(0)

        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponse('Success')
            else:
                return HttpResponse('inactive user')
        else:
            return HttpResponse('Bad request')


def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            full_name = form.cleaned_data.get('full_name')
            username = full_name if full_name else f'acc_{User.objects.count() + 1}'

            user = User.objects.create_user(username=username,
                                            email=form.cleaned_data.get('email'),
                                            password=form.cleaned_data.get('password1'))
            user.save()
            doctor = Doctor(
                user=user,
                full_name=full_name,
                qualification=form.cleaned_data.get('qualification'),
                experience=form.cleaned_data.get('experience'),
                work_place=form.cleaned_data.get('work_place'),
                education=form.cleaned_data.get('education'),
                contacts=form.cleaned_data.get('contacts'),
                photo=form.cleaned_data.get('photo'),
            )
            doctor.save()

            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user_a = authenticate(email=email, password=raw_password,
                                  backend='django.contrib.auth.backends.EmailBackend')
            login(request, user)
            return redirect('cabinet')
    else:
        form = SignUpForm()
    return render(request, 'registration/sign_up.html', {'form': form})


class DoctorsListView(LoginRequiredMixin, generic.ListView):
    login_url = LOGIN_URL
    template_name = 'doctor_list.html'
    model = Doctor

    def get_queryset(self):
        search_query = self.request.GET.get('q')
        search_query = search_query if search_query else ''
        return Doctor.objects.filter(
            Q(full_name__icontains=search_query) |
            Q(qualification__icontains=search_query)
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['get_queryset'] = self.get_queryset()
        return context


def reference_view(request):
    faq = FAQ.objects.first()
    return render(request, 'reference.html',
                  context={
                      'FAQItems': FAQItem.objects.filter(reference=faq)
                  })
