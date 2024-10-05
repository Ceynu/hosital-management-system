from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Doctor, Appointment, PatientRecord

admin.site.register(Doctor)
admin.site.register(Appointment)
admin.site.register(PatientRecord)

