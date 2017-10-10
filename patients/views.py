from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect, requires_csrf_token
from .models import Patient

@login_required(login_url="/")
def add_patient(request):
    return render(request, "patients/add_patient.html")

@login_required(login_url="/")
def patient_added(request):
    try:
        forename = request.POST['forename']
        surname = request.POST['surname']
        dob = request.POST['dob']
        nhs_number = request.POST['nhs_number']
        sex = request.POST['sex']
        ethnicity = request.POST['ethnicity']
        first_incident = request.POST['#1_incident']
        dead_censor = request.POST['dead_censor']
        snumber = request.POST['snumber']
        if request.POST['deceased'] is 'True':
            deceased = True
        else:
            deceased = False
        patient = Patient(forename=forename, surname=surname, DOB=dob, nhs_number=nhs_number, sex=sex,
                          ethnicity=ethnicity, first_incident=first_incident, DOD_DOC=dead_censor,
                          hospital_number=snumber, deceased=deceased)
        patient.save()
        return render(request, "patients/patient_added.html", {'patient': str(nhs_number) +' added successfully'})
    except Exception:
        return render(request, "patients/patient_added.html", {'patient': 'Error: patient not added'})
