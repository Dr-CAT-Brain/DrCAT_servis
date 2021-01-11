from django.contrib import admin
from .models import Diagnosis, Patient


@admin.register(Diagnosis)
class DiagnosesAdmin(admin.ModelAdmin):
    pass


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    pass
