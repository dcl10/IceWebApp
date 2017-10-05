from django.db import models

# Create your models here.
class Patient(models.Model):

    forename = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    DOB = models.CharField(max_length=15)
    nhs_number = models.CharField(max_length=20, primary_key=True, unique=True)
    sex = models.CharField(max_length=1)
    ethnicity = models.CharField(max_length=30)
    first_incident = models.CharField(max_length=15)
    DOD_DOC = models.CharField(max_length=15)
    hospital_number = models.CharField(max_length=20)
    deceased = models.BooleanField()

    def __str__(self):
        return self.nhs_number