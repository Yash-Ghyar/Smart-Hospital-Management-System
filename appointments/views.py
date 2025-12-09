from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Appointment


@login_required
def appointment_list(request):
    if request.user.is_superuser:
        appointments = Appointment.objects.select_related("doctor__user", "patient__user").all()
    elif hasattr(request.user, "doctor"):
        appointments = Appointment.objects.filter(doctor=request.user.doctor)
    elif hasattr(request.user, "patient"):
        appointments = Appointment.objects.filter(patient=request.user.patient)
    else:
        appointments = Appointment.objects.none()

    appointments = appointments.order_by("-date", "-time")

    return render(request, "appointments/list.html", {"appointments": appointments})
