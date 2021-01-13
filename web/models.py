from django.db import models
from django.utils.html import mark_safe
from django.conf import settings


class Diagnosis(models.Model):
    name = models.CharField(max_length=200, null=False)
    description = models.TextField(null=True)

    def __str__(self):
        return self.name


class Patient(models.Model):
    full_name = models.CharField(max_length=100, null=True)
    age = models.PositiveSmallIntegerField(null=True)

    diagnoses = models.ManyToManyField(Diagnosis, null=True)

    def __str__(self):
        return self.full_name


class Treatment(models.Model):
    conscious_level = models.CharField(max_length=100, null=True)
    general_state = models.PositiveSmallIntegerField(null=True)

    hematoma_volume = models.PositiveSmallIntegerField(null=True)

    coagupathy = models.BooleanField(default=False)
    takes_anticoagulants = models.BooleanField(default=False)

    time_passed = models.PositiveSmallIntegerField(null=True)
    snapshot = models.ImageField(upload_to='snapshots', null=True)

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.patient.full_name

    def admin_list_item_image(self):
        width = 270
        height = 150
        return mark_safe(f'<img src="{settings.MEDIA_URL}{self.snapshot}" width="{width}" height="{height}" />')
