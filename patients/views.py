from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from appointments.forms import AppointmentForm
from appointments.models import Appointment
from .forms import PatientProfileForm
from .models import Patient


@login_required
def patient_dashboard(request):
    if not hasattr(request.user, "patient"):
        return redirect("home")

    patient = request.user.patient

    appointments = (
        Appointment.objects.filter(patient=patient)
        .select_related("doctor__user")
        .order_by("-date", "-time")
    )

    history = patient.history.all().order_by("-test_date")

    context = {
        "patient": patient,
        "appointments": appointments,
        "history": history,
    }
    return render(request, "patients/patient_dashboard.html", context)


@login_required
def patient_profile_edit(request):
    if not hasattr(request.user, "patient"):
        return redirect("home")

    patient = request.user.patient

    if request.method == "POST":
        form = PatientProfileForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            return redirect("patient_dashboard")
    else:
        form = PatientProfileForm(instance=patient)

    return render(request, "patients/patient_profile.html", {"form": form})


@login_required
def book_appointment(request):
    if not hasattr(request.user, "patient"):
        return redirect("home")

    patient = request.user.patient

    if request.method == "POST":
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.patient = patient
            appointment.status = "PENDING"
            appointment.save()
            return redirect("patient_dashboard")
    else:
        form = AppointmentForm()

    return render(request, "patients/book_appointment.html", {"form": form})
