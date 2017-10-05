from django.db import models
from patients.models import Patient

# Create your models here.
class Report(models.Model):
    report_id = models.CharField(max_length=20, primary_key=True, unique=True)
    report_type = models.CharField(max_length=50)
    reporting_clinician = models.CharField(max_length=50)
    report_date = models.DateField()
    nhs_number = models.ForeignKey(Patient, on_delete=models.CASCADE)
    body = models.TextField()

    def __str__(self):
        return self.report_id

