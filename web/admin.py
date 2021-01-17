from django.contrib import admin
from .models import *


class TreatmentInline(admin.TabularInline):
    model = Treatment
    extra = 0


@admin.register(Diagnosis)
class DiagnosesAdmin(admin.ModelAdmin):
    pass


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    inlines = [TreatmentInline]


@admin.register(Treatment)
class Treatment(admin.ModelAdmin):
    list_display = ["get_snapshot_html", "patient"]


@admin.register(TemporaryContraindications)
class TemporaryContraindications(admin.ModelAdmin):
    pass


admin.site.site_header = 'Admin-panel'
admin.site.index_title = 'Databases'
