from django import forms
from django.core.exceptions import ValidationError
from django.core.files.storage import FileSystemStorage
from django.utils.translation import ugettext_lazy as _
import datetime
from .models import Diagnosis


def get_placeholder_widget(name):
    return forms.TextInput(attrs={'placeholder': name})


class TreatmentForm(forms.Form):
    full_name = forms.CharField(max_length=100, required=False,
                                widget=get_placeholder_widget('ФИО'))

    age = forms.IntegerField(max_value=100, min_value=1, required=False,
                             widget=get_placeholder_widget('Возраст'))

    conscious_level = forms.CharField(min_length=1, max_length=100,
                                      widget=get_placeholder_widget("Уровень сознания"))

    diagnoses = forms.ModelMultipleChoiceField(
        queryset=Diagnosis.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        label="Загрузите изображение",
        required=False,
    )

    hematoma_volume = forms.IntegerField(max_value=200, required=False,
                                         widget=get_placeholder_widget("Объем внутримозговой гематомы"))

    coagupathy = forms.BooleanField(required=False, initial=False)
    takes_anticoagulants = forms.BooleanField(required=False, initial=False)

    time_passed = forms.IntegerField(min_value=0, required=True,
                                     widget=get_placeholder_widget("Время от начала симптомов"))
    is_injure = forms.BooleanField(required=False, initial=False)
    snapshot = forms.ImageField()
