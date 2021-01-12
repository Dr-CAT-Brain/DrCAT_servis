from django.db import models


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
        return self.name.capitalize()


class Treatment(models.Model):
    conscious_level = models.CharField(max_length=100, null=True)
    general_state = models.PositiveSmallIntegerField(null=True)

    hematoma_volume = models.PositiveSmallIntegerField(null=True)

    coagupathy = models.BooleanField(default=False)
    takes_anticoagulants = models.BooleanField(default=False)

    time_passed = models.PositiveSmallIntegerField(null=True)
    snapshot = models.ImageField(upload_to='snapshots', null=True)
