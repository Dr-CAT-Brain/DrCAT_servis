from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import *


def test_form(request):
    return render(request, 'form_test.html')


def success(request):
    return 'success!'


def treatment_form_view(request):
    if request.method == 'POST':
        form = TreatmentForm(request.POST, request.FILES)

        if form.is_valid():
            return HttpResponseRedirect('/success')

    else:
        form = TreatmentForm(initial={'name': 'David', })

    return render(request, 'form_test.html', {'form': form})
