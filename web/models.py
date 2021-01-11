from django.db import models


class Diagnosis(models.Model):
    name = models.CharField(max_length=200, null=False)
    description = models.TextField(null=True)

    def __str__(self):
        return self.name


class Patient(models.Model):
    name = models.CharField(max_length=50, null=True)
    surname = models.CharField(max_length=50, null=True)
    age = models.PositiveSmallIntegerField()
    diagnoses = models.ManyToManyField(Diagnosis)

    def __str__(self):
        return self.name.capitalize()


