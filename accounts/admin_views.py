from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from doctors.models import Doctor
from patients.models import Patient
from appointments.models import Appointment

@login_required
def manage_doctors(request):
    doctors = Doctor.objects.all()
    return render(request, "accounts/manage_doctors.html", {"doctors": doctors})

@login_required
def manage_patients(request):
    patients = Patient.objects.all()
    return render(request, "accounts/manage_patients.html", {"patients": patients})

@login_required
def manage_appointments(request):
    appointments = Appointment.objects.all()
    return render(request, "accounts/manage_appointments.html", {"appointments": appointments})
