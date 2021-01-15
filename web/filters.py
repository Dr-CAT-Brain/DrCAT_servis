import django_filters
from django import forms

from .models import Treatment


class TreatmentFilter(django_filters.FilterSet):
    conscious_level = django_filters.CharFilter(lookup_expr='iexact')

    hematoma_volume = django_filters.RangeFilter(label="Объем гематомы")
    general_state = django_filters.RangeFilter(label="Общее состояние")
    conscious_level = django_filters.RangeFilter(label="Уровень сознания")
    time_passed = django_filters.NumberFilter(label="Время после симптомов")
    coagupathy = django_filters.BooleanFilter(label="Коагуапатия", widget=forms.CheckboxInput)
    takes_anticoagulants = django_filters.BooleanFilter(label="Принимает антикоагулянты",
                                                        widget=forms.CheckboxInput)

    is_injury = django_filters.BooleanFilter(label='Травма', widget=forms.CheckboxInput)

    class Meta:
        model = Treatment
        fields = {}
