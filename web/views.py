import os
import pathlib

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.decorators import method_decorator
from django.views import generic
from .filters import TreatmentFilter
from .LabelDecoder import decode_label
from neuronet.model_predict import predict_picture

from .forms import *
from .models import Patient, Treatment, NeuronetPrediction
from neuronet.recomendation_algo import give_recommend


@login_required
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

    history = Treatment.objects.filter(doctor=doctor).all()

    return render(request, 'cabinet.html',
                  context={'header': 'Личный кабинет',
                           'doctor': request.user.doctor,
                           'form': form,
                           'history': history,
                           })


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

            treatment.snapshot = form.cleaned_data['snapshot']
            treatment.patient = patient

            if request.user:
                treatment.doctor = request.user.doctor
            treatment.save()

            for diagnosis in form.cleaned_data['diagnoses'].iterator():
                patient.diagnoses.add(diagnosis)

            for contraindications in form.cleaned_data['temporary_contraindications'].iterator():
                treatment.temporary_contraindications.add(contraindications)

            treatment.save()
            patient.save()

            image_absolute_path = get_absolute_path_to_project() + treatment.snapshot.url
            # 1. Конвертируем полученную табличку в число
            # 2. Сохраняем число
            # 3. Сохраняем вероятность
            # 4. Получаем рекомендации
            # 5. Сохраняем рекомендации
            prediction = predict_picture(image_absolute_path)
            prediction.recommend_text = give_recommend(prediction.classification_type,
                                                       treatment.neurological_deficit,
                                                       treatment.conscious_level,
                                                       treatment.time_passed,
                                                       treatment.hematoma_volume,
                                                       treatment.is_injury,
                                                       treatment.has_stroke_symptoms,
                                                       treatment.patient.get_diagnoses_name_list(),
                                                       treatment.get_temporary_contraindications_name_list())
            prediction.save()
            treatment.predict = prediction
            treatment.save()

            return HttpResponseRedirect(f'report/{treatment.id}')
    else:
        form = TreatmentForm()

    return render(request, 'treatment_form.html', {'form': form})


class TreatmentListView(generic.ListView):
    # paginate_by = 10
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
        context['predicted_diagnosis'] = decode_label(treatment.predict.classification_type)
        # context['operation_text'] = treatment.predict.recommen
        return context


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
