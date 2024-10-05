from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100)
    contact_info = models.CharField(max_length=100)
    consultation_fee = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class Appointment(models.Model):
    patient = models.ForeignKey(User, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    appointment_date = models.DateTimeField()
    status = models.CharField(max_length=50, default='Pending')

    def __str__(self):
        return f'{self.patient.username} - {self.doctor.name} - {self.appointment_date}'


class PatientRecord(models.Model):
    patient = models.ForeignKey(User, on_delete=models.CASCADE)
    medical_record = models.TextField()

    def __str__(self):
        return f'Medical record of {self.patient.username}'

