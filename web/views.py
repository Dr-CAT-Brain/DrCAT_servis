from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import *
from .models import Patient, Treatment, Diagnosis


def index(request):
    return render(request, "start_page.html")


def test_form(request):
    return render(request, 'form_test.html')


@login_required
def cabinet_view(request):
    return render(request, 'cabinet.html')


def success(request):
    return render(request, 'success.html')


def treatment_form_view(request):
    if request.method == 'POST':
        form = TreatmentForm(request.POST, request.FILES)

        if form.is_valid():
            patient = Patient()
            treatment = Treatment()

            patient.full_name = form.cleaned_data['full_name']
            patient.age = form.cleaned_data['age']

            treatment.conscious_level = form.cleaned_data['conscious_level']
            treatment.general_state = form.cleaned_data['general_state']
            treatment.hematoma_volume = form.cleaned_data['hematoma_volume']
            treatment.coagupathy = form.cleaned_data['coagupathy']
            treatment.takes_anticoagulants = form.cleaned_data['takes_anticoagulants']
            treatment.time_passed = form.cleaned_data['time_passed']
            treatment.snapshot = form.cleaned_data['snapshot']
            treatment.patient = patient
            patient.save()

            for diagnosis in form.cleaned_data['diagnoses'].iterator():
                patient.diagnoses.add(diagnosis)

            treatment.save()
            patient.save()

            return HttpResponseRedirect('/success')

    else:
        form = TreatmentForm(initial={'name': 'David', })

    return render(request, 'form_test.html', {'form': form})
