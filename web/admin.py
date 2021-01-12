from django.contrib import admin
from .models import Diagnosis, Patient, Treatment


@admin.register(Diagnosis)
class DiagnosesAdmin(admin.ModelAdmin):
    pass


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    pass


@admin.register(Treatment)
class Treatment(admin.ModelAdmin):
    pass
