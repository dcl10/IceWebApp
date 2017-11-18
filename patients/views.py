from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect, requires_csrf_token
from .models import Patient
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render


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
        if request.POST['deceased'] == 'True':
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


@login_required(login_url="/")
def list_patients(request):
    patient_list = Patient.objects.all()
    paginator = Paginator(patient_list, 15)
    page = request.GET.get('page')
    try:
        patients = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        patients = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        patients = paginator.page(paginator.num_pages)

    return render(request, 'patients/patients.html', {'patients': patients})
