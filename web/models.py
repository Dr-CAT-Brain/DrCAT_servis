from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.html import mark_safe
from django.conf import settings
from .LabelDecoder import decode_label, decode_label_detail


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

    diagnoses = models.ManyToManyField(Diagnosis, blank=True)

    def __str__(self):
        return self.full_name

    def get_diagnoses_name_list(self):
        if self.diagnoses:
            return [i.name for i in self.diagnoses.all()]
        return []


class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    full_name = models.CharField(max_length=100, null=False, blank=False, default='Фамилия имя отчество')
    qualification = models.CharField(max_length=100, null=True, blank=True)
    experience = models.PositiveSmallIntegerField(null=True, blank=True)
    work_place = models.CharField(max_length=100, null=True, blank=True)
    education = models.CharField(max_length=100, null=True, blank=True)
    contacts = models.CharField(max_length=100, null=True, blank=True)
    photo = models.ImageField(null=True, default='profile_photo.jpg')

    def __str__(self):
        return f'{self.full_name} {self.user.username}'


class RecommendText(models.Model):
    operation = models.CharField(max_length=100)
    treatment_tactics = models.TextField()
    tactics_if_agree = models.TextField()


class NeuronetPrediction(models.Model):
    classification_type = models.PositiveSmallIntegerField(null=True)
    confidence = models.FloatField(null=True)

    recommend_text = models.OneToOneField(RecommendText, on_delete=models.CASCADE)

    def __str__(self):
        return f'{decode_label(self.classification_type)} : {format(self.confidence, ".2f")}%'


class Treatment(models.Model):
    neurological_deficit = models.PositiveSmallIntegerField(null=False, default=1)
    conscious_level = models.PositiveSmallIntegerField(null=False, default=15)

    time_passed = models.PositiveSmallIntegerField(null=True, blank=True)
    hematoma_volume = models.PositiveSmallIntegerField(null=True, blank=True)

    is_injury = models.BooleanField(default=False, null=True, blank=True)
    has_stroke_symptoms = models.BooleanField(default=False, null=False)

    temporary_contraindications = models.ManyToManyField(TemporaryContraindications, blank=True)

    snapshot = models.ImageField(upload_to='snapshots', null=True, blank=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True, blank=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, null=True, default=None, blank=True)

    predict = models.OneToOneField(NeuronetPrediction,
                                   on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        patology = ''
        if self.predict:
            patology = decode_label_detail(self.predict.classification_type)
        return f'{self.patient.full_name}.{patology} '

    def get_snapshot_html(self):
        return mark_safe(f'<img src="{settings.MEDIA_URL}{self.snapshot}" alt="File image"/>')

    def get_absolute_url(self):
        return reverse('treatment_detail', args=[str(self.id)])

    def get_temporary_contraindications_name_list(self):
        if self.temporary_contraindications:
            return [i.name for i in self.temporary_contraindications.all()]
        return []
