from django.conf.urls import url
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views_test import treatment_form_short_view

from . import views

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('cabinet/', views.cabinet_view, name='cabinet'),
    url(r'^profile/(?P<pk>\d+)$', views.DoctorProfileDetailView.as_view(), name='profile'),
    path('peoples/', views.DoctorsListView.as_view(), name='peoples'),
    path('treatment-form', views.treatment_form_view, name='treatment_form'),
    path('treatment-form-short', treatment_form_short_view),
    url(r'^report/(?P<pk>\d+)$', views.TreatmentDetailView.as_view(), name='treatment_report'),
    path('treatment-list/', views.TreatmentListView.as_view(), name='treatment_list'),
    path('history', views.TreatmentHistoryView.as_view(), name='history_list'),
    url(r'^treatment/(?P<pk>\d+)$', views.TreatmentDetailView.as_view(), name='treatment_detail'),
    url('api/login', views.api_login),
    path('signup/', views.sign_up, name='sign_up'),
    path('FAQ/', views.reference_view, name='reference'),
    path('refit_knn', views.refit_knn, name='refit_knn'),
    url('formalize_document/(?P<pk>\d+)$', views.formalize_treatment_to_document, name='formalize_document'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
