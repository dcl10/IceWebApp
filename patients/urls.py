from django.conf.urls import url
from django.views.generic import ListView, DetailView
from patients.models import Patient
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    url(r'^$', login_required(ListView.as_view(queryset=Patient.objects.all(), template_name="patients/patients.html"),
                              login_url="/")),
    url(r'^(?P<pk>\d+)$', login_required(DetailView.as_view(model=Patient, template_name="patients/info.html"),
                                         login_url="/")),
    url(r'^add/', views.add_patient),
    url(r'^added/', views.patient_added)
]