from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views import generic
from .filters import TreatmentFilter

from .forms import *
from .models import Patient, Treatment, Diagnosis


def index(request):
    return render(request, "index.html")


def test_form(request):
    return render(request, 'form_test.html')


@login_required
def cabinet_view(request):
    return render(request, 'cabinet.html')


def treatment_report(request):
    return render(request, 'treatment_report.html')


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
            treatment.is_injury = form.cleaned_data['is_injure']
            treatment.patient = patient
            patient.save()

            for diagnosis in form.cleaned_data['diagnoses'].iterator():
                patient.diagnoses.add(diagnosis)

            treatment.save()
            patient.save()

            return HttpResponseRedirect('report')

    else:
        form = TreatmentForm(initial={'name': 'David', })

    return render(request, 'form_test.html', {'form': form})


class TreatmentListView(generic.ListView):
    # paginate_by = 10
    model = Treatment
    template_name = 'treatment_list.html'

    def get_ordering(self):
        ordering = self.request.GET.get('ordering', 'hematoma_volume')
        return ordering

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = TreatmentFilter(self.request.GET, queryset=Treatment.objects.all())
        return context


class TreatmentsDetailView(generic.DetailView):
    model = Treatment
    template_name = "treatment_detail.html"

