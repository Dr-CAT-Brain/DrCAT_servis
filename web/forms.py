from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from .models import Diagnosis, TemporaryContraindications


def get_placeholder_widget(name, css_class=None):
    return forms.TextInput(attrs={'placeholder': name,
                                  'class': css_class})


def choice_to_bool(string: str) -> bool:
    choice_to_bool_dict = {
        'yes': True,
        'no': False,
        'unknown': None
    }

    return choice_to_bool_dict[string.lower()]


class TreatmentForm(forms.Form):
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
        widget=forms.RadioSelect,
        initial=1,
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

    snapshot = forms.ImageField(required=True)

    def clean_snapshot(self):
        data = self.cleaned_data['snapshot']
        return data


class PersonalData(forms.Form):
    full_name = forms.CharField(max_length=100, required=True, label='ФИО')
    qualification = forms.CharField(max_length=100, required=False, label='Квалификация')
    experience = forms.IntegerField(min_value=0, max_value=70, required=False, label='Стаж')
    work_place = forms.CharField(max_length=100, required=False, label='Место работы')
    education = forms.CharField(max_length=100, required=False, label='Образование')
    contacts = forms.CharField(max_length=100, required=False, label='Контакты')
    image = forms.ImageField(required=False, allow_empty_file=False)


class SignUpForm(UserCreationForm):
    full_name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(max_length=254, required=True)
    password1 = forms.CharField(widget=forms.PasswordInput())
    qualification = forms.CharField(max_length=40, required=False)
    work_place = forms.CharField(max_length=60, required=False)
    education = forms.CharField(max_length=30, required=False)
    experience = forms.IntegerField(min_value=0, required=False)
    contacts = forms.CharField(max_length=150, required=False)
    photo = forms.ImageField(required=True)

    class Meta:
        model = User
        fields = ('full_name', 'email', 'password1', 'qualification', 'work_place',
                  'education', 'experience', 'contacts', 'photo')

