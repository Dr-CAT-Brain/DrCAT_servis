from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.html import mark_safe
from django.conf import settings


class Diagnosis(models.Model):
    name = models.CharField(max_length=200, null=False)
    description = models.TextField(null=True, blank=True)
    text_to_onclusion = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class TemporaryContraindications(models.Model):
    name = models.CharField(max_length=200, null=False)
    description = models.TextField(null=True, blank=True)
    text_to_onclusion = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Patient(models.Model):
    full_name = models.CharField(max_length=100, null=True, blank=True)
    age = models.PositiveSmallIntegerField(null=True, blank=True)

    diagnoses = models.ManyToManyField(Diagnosis)

    def __str__(self):
        return self.full_name


class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    full_name = models.CharField(max_length=100, null=False, blank=False, default='Фамилия Имя Отчество')
    qualification = models.CharField(max_length=100, null=True, blank=True)
    experience = models.PositiveSmallIntegerField(null=True, blank=True)
    work_place = models.CharField(max_length=100, null=True, blank=True)
    education = models.CharField(max_length=100, null=True, blank=True)
    contacts = models.CharField(max_length=100, null=True, blank=True)
    photo = models.ImageField(null=True, default='BaseProfilePhoto.svd')

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}; username: {self.user.username}'


class ClassificationTypes:
    VMG = 0


class NeuronetPrediction(models.Model):
    classification_type = models.PositiveSmallIntegerField(null=False)
    confidence = models.PositiveSmallIntegerField(null=True)


class Treatment(models.Model):
    neurological_deficit = models.PositiveSmallIntegerField(null=False, default=1)
    conscious_level = models.PositiveSmallIntegerField(null=False, default=15)

    time_passed = models.PositiveSmallIntegerField(null=True, blank=True)
    hematoma_volume = models.PositiveSmallIntegerField(null=True, blank=True)

    is_injury = models.BooleanField(default=False, null=True, blank=True)
    has_stroke_symptoms = models.BooleanField(default=False, null=False)

    temporary_contraindications = models.ManyToManyField(TemporaryContraindications)

    snapshot = models.ImageField(upload_to='snapshots', null=True, blank=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True, blank=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, null=True, default=None, blank=True)

    predict = models.OneToOneField(NeuronetPrediction,
                                     on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.patient.full_name

    def get_snapshot_html(self):
        width = 270
        height = 150
        return mark_safe(f'<img src="{settings.MEDIA_URL}{self.snapshot}" width="{width}" height="{height}" />')

    def get_absolute_url(self):
        return reverse('treatment_detail', args=[str(self.id)])
