from django import forms
from django.core.exceptions import ValidationError
from django.core.files.storage import FileSystemStorage
from django.utils.translation import ugettext_lazy as _
import datetime
from .models import Diagnosis


class TreatmentForm(forms.Form):
    full_name = forms.CharField(max_length=50, help_text="Введите")
    age = forms.IntegerField(max_value=100, min_value=1)

    conscious_level = forms.CharField(min_length=1, max_length=100, help_text="Уровень сознания")
    general_state = forms.IntegerField(min_value=0, max_value=6, help_text="Общее состояние")

    diagnoses = forms.ModelMultipleChoiceField(
        queryset=Diagnosis.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        help_text="Диагнозы",
        required=False,
    )

    hematoma_volume = forms.IntegerField(max_value=200, help_text="Объем внутримозговой гематомы",
                                         required=False)

    coagupathy = forms.BooleanField(help_text="Коагупатия", required=True)
    takes_anticoagulants = forms.BooleanField(help_text="Прием антикоагулянтов", required=True)

    time_passed = forms.IntegerField(min_value=0, help_text="Время от начала симптомов", required=True)

    shapshot = forms.ImageField()

    def clean_renewal_date(self):
        data = self.cleaned_data['renewal_date']

        if data < datetime.date.today():
            raise ValidationError(_('Invalid date - renewal in past'))

        if data > datetime.date.today() + datetime.timedelta(weeks=4):
            raise ValidationError(_('Invalid date - renewal more than 4 weeks ahead'))

        return data
