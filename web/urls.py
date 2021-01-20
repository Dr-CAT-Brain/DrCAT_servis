from django.conf.urls import url
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('pass', lambda x: x, name='pass'),
    path('cabinet/', views.cabinet_view, name='cabinet'),
    path('treatment-form', views.treatment_form_view, name='treatment_form'),
    url(r'^report/(?P<pk>\d+)$', views.TreatmentDetailView.as_view(), name='treatment_report'),
    path('treatment-list', views.TreatmentListView.as_view(), name='treatment_list'),
    path('history', views.TreatmentHistoryView.as_view(), name='history_list'),
    url(r'^treatment/(?P<pk>\d+)$', views.TreatmentDetailView.as_view(), name='treatment_detail'),
    url('api/login', views.api_login)
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
