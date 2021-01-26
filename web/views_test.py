from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from neuronet.recomendation import adapt_int_to_patology, get_recommendations
from .models import Patient, Treatment, ClassificationType, NeuronetPrediction, Diagnosis, TemporaryContraindications


def get_placeholder_widget(name, css_class=None):
    return forms.TextInput(attrs={'placeholder': name,
                                  'class': css_class})


class TreatmentFormShort(forms.Form):
    unknown_text = 'Неизвестно'
    unknown_placeholder = get_placeholder_widget(unknown_text)

    full_name = forms.CharField(max_length=100, required=False, label='ФИО пациента',
                                widget=unknown_placeholder)
    age = forms.IntegerField(max_value=100, min_value=1, required=False,
                             label='Возраст', widget=get_placeholder_widget(unknown_text, 'num'))

    time_passed = forms.IntegerField(min_value=0, required=False,
                                     label="Время начала симптоматики (ч)", widget=unknown_placeholder)
    hematoma_volume = forms.IntegerField(max_value=200, required=False,
                                         label="Объем гематомы (см³)",
                                         widget=get_placeholder_widget(unknown_text, 'num-2'))

    is_injure = forms.ChoiceField(
        choices=[(True, 'Да'), (False, 'Нет'), (None, 'Неизвестно')],
        initial=None,
        label='Травма',
        required=False,
        widget=forms.RadioSelect,
    )

    has_stroke_symptoms = forms.ChoiceField(required=False,
                                            label='Симптомы инусльта',
                                            choices=[(True, 'Да'), (False, 'Нет')],
                                            initial=True,
                                            widget=forms.RadioSelect)

    neurological_deficit = forms.ChoiceField(
        choices=[(1, 'I'), (2, 'II'), (3, 'III'), (4, 'IV')],
        initial=1,
        widget=forms.RadioSelect,
        label='Неврологический дефицит*'
    )

    conscious_level = forms.ChoiceField(
        choices=[(15, '15 Ясное'), (14, '14-13 Умеренное оглушение'), (12, '12-11 Глубокое оглушение'),
                 (9, '10-8 Сопор'), (7, 'Умеренная кома'), (5, 'Глубокая кома'), (3, 'Терминальная кома')],
        initial=15,
        widget=forms.RadioSelect,
        label='Неврологический дефицит*'
    )

    diagnoses = forms.ModelMultipleChoiceField(
        queryset=Diagnosis.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        label="Сопутствующие паталогии",
        required=False,
    )

    temporary_contraindications = forms.ModelMultipleChoiceField(
        queryset=TemporaryContraindications.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        label="Иные противопоказания",
        required=False,
    )

    patology_type = forms.ChoiceField(
        choices=[(0, 'ВЖК'), (1, 'ВМГ + ВЖК'), (2, 'ВМГ+Зад. ямка'), (3, 'ВМГ конс'),
                 (4, 'ВМГ опер'), (5, 'Ишемия'), (6, 'Ишемия + реперфуз'), (7, 'Опухоль'),
                 (8, 'САК'), (9, 'САК + ВМГ')],
        initial=1,
    )

    def clean_snapshot(self):
        data = self.cleaned_data['snapshot']
        return data


def treatment_form_short_view(request):
    if request.method == 'POST':
        form = TreatmentFormShort(request.POST, request.FILES)
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

            treatment.snapshot = Treatment.objects.first().snapshot
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

            prediction = NeuronetPrediction(
                confidence=1
            )
            prediction.save()

            classification_type = ClassificationType.objects.create(
                value=form.cleaned_data['patology_type'],
                prediction=prediction
            )
            prediction.classification_types.add(classification_type)
            prediction.save()

            patologies = []
            for i in ClassificationType.objects.filter(prediction=prediction).all():
                patologies.append(adapt_int_to_patology(i.value, treatment))

            prediction.recommend_text = get_recommendations(patologies)
            prediction.save()

            treatment.predict = prediction
            treatment.save()

            return HttpResponseRedirect(f'report/{treatment.id}')
    else:
        form = TreatmentFormShort()

    return render(request, 'treatment_form_short.html', {'form': form})
