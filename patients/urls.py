from django.conf.urls import url
from django.views.generic import ListView, DetailView
from patients.models import Patient
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    url(r'^$', views.list_patients),
    url(r'^(?P<pk>\d+)$', login_required(DetailView.as_view(model=Patient, template_name="patients/info.html"),
                                         login_url="/")),
    url(r'^add/', views.add_patient),
    url(r'^added/', views.patient_added)
]