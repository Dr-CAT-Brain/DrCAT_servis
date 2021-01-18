from django.db import models
from django.urls import reverse
from django.utils.html import mark_safe
from django.conf import settings


class Diagnosis(models.Model):
    name = models.CharField(max_length=200, null=False)
    description = models.TextField(null=True)
    text_to_onclusion = models.TextField(null=True)

    def __str__(self):
        return self.name


class TemporaryContraindications(models.Model):
    name = models.CharField(max_length=200, null=False)
    description = models.TextField(null=True)
    text_to_onclusion = models.TextField(null=True)

    def __str__(self):
        return self.name


class Patient(models.Model):
    full_name = models.CharField(max_length=100, null=True)
    age = models.PositiveSmallIntegerField(null=True)

    diagnoses = models.ManyToManyField(Diagnosis)

    def __str__(self):
        return self.full_name


class Treatment(models.Model):
    conscious_level = models.PositiveSmallIntegerField(null=False, default=1)
    neurological_deficit = models.PositiveSmallIntegerField(null=False, default=15)

    time_passed = models.PositiveSmallIntegerField(null=True)
    hematoma_volume = models.PositiveSmallIntegerField(null=True)

    is_injury = models.BooleanField(default=False, null=True)
    has_stroke_symptoms = models.BooleanField(default=False, null=False)

    temporary_contraindications = models.ManyToManyField(TemporaryContraindications)

    snapshot = models.ImageField(upload_to='snapshots', null=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.patient.full_name

    def get_snapshot_html(self):
        width = 270
        height = 150
        return mark_safe(f'<img src="{settings.MEDIA_URL}{self.snapshot}" width="{width}" height="{height}" />')

    def get_absolute_url(self):
        return reverse('treatment_detail', args=[str(self.id)])
