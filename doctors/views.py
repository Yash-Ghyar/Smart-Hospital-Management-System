from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from appointments.models import Appointment
from .forms import DoctorProfileForm, AvailabilityForm
from .models import Doctor


@login_required
def doctor_dashboard(request):
    if not hasattr(request.user, "doctor"):
        return redirect("home")

    doctor = request.user.doctor
    appointments = (
        Appointment.objects.filter(doctor=doctor)
        .select_related("patient__user")
        .order_by("date", "time")
    )
    slots = doctor.availabilities.all().order_by("day", "start_time")

    context = {
        "doctor": doctor,
        "appointments": appointments,
        "slots": slots,
    }
    return render(request, "doctors/doctor_dashboard.html", context)


@login_required
def doctor_profile_edit(request):
    if not hasattr(request.user, "doctor"):
        return redirect("home")

    doctor = request.user.doctor

    if request.method == "POST":
        form = DoctorProfileForm(request.POST, instance=doctor)
        if form.is_valid():
            form.save()
            return redirect("doctor_dashboard")
    else:
        form = DoctorProfileForm(instance=doctor)

    return render(request, "doctors/doctor_profile.html", {"form": form})


@login_required
def add_slot(request):
    if not hasattr(request.user, "doctor"):
        return redirect("home")

    doctor = request.user.doctor

    if request.method == "POST":
        form = AvailabilityForm(request.POST)
        if form.is_valid():
            slot = form.save(commit=False)
            slot.doctor = doctor
            slot.save()
            return redirect("doctor_dashboard")
    else:
        form = AvailabilityForm()

    return render(request, "doctors/add_slot.html", {"form": form})
