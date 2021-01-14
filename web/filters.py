import django_filters

from .models import Treatment


class TreatmentFilter(django_filters.FilterSet):
    FILTER_CHOICES = (
        ('hematoma_volume', 'Объем гематомы (возрастание)'),
        ('-hematoma_volume', 'Объем гематомы (убывание)'),
    )

    ordering = django_filters.ChoiceFilter(label="Order by", choices=FILTER_CHOICES, method="get_order_by")

    def get_order_by(self, queryset, name, value):
        return queryset.order_by(value)

    class Meta:
        model = Treatment
        fields = {
            'hematoma_volume': ['range'],
        }
