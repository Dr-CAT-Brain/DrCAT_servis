import django_filters
from django import forms

from .models import Treatment, Diagnosis, TemporaryContraindications


class TreatmentFilter(django_filters.FilterSet):
    conscious_level = django_filters.CharFilter(lookup_expr='iexact', label='Уровень сознания')
    neurological_deficit = django_filters.RangeFilter(label='Неврологический дефицит')

    hematoma_volume = django_filters.RangeFilter(label="Объем гематомы")
    conscious_level = django_filters.RangeFilter(label="Уровень сознания")
    time_passed = django_filters.RangeFilter(label="Время после симптомов")

    bool_choices = (
        (True, "Да"),
        (False, "Нет"),
        (None, "Неважно")
    )
    is_injury = django_filters.ChoiceFilter(label='Травма', choices=bool_choices,
                                            widget=forms.RadioSelect, empty_label=None)
    has_stroke_symptoms = django_filters.ChoiceFilter(label='Симптомы инсульта', choices=bool_choices,
                                                      widget=forms.RadioSelect, empty_label=None)

    temporary_contraindications = django_filters.ModelMultipleChoiceFilter(
        to_field_name='id',
        queryset=TemporaryContraindications.objects.all(),
        label='Иные противопоказания', )

    class Meta:
        model = Treatment
        fields = {}

