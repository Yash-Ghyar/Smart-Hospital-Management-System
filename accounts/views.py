from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from doctors.models import Doctor
from patients.models import Patient
from appointments.models import Appointment


def home_view(request):
    return render(request, "home.html")


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            if user.is_superuser:
                return redirect("admin_dashboard")
            if hasattr(user, "doctor"):
                return redirect("doctor_dashboard")
            if hasattr(user, "patient"):
                return redirect("patient_dashboard")

            return redirect("home")
        else:
            messages.error(request, "Invalid username or password.")

    return render(request, "accounts/login.html")


def logout_view(request):
    logout(request)
    return redirect("login")


def patient_signup_view(request):
    if request.method == "POST":
        username = request.POST.get("username").strip()
        password = request.POST.get("password").strip()
        confirm = request.POST.get("confirm_password").strip()

        full_name = request.POST.get("full_name").strip()
        phone = request.POST.get("phone").strip()

        if password != confirm:
            messages.error(request, "Passwords do not match.")
            return redirect("patient_signup")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken.")
            return redirect("patient_signup")

        # Create user
        user = User.objects.create_user(
            username=username,
            password=password,
            first_name=full_name,
        )

        # Create patient profile
        Patient.objects.create(
            user=user,
            phone=phone,
        )

        messages.success(request, "Patient account created. Please login.")
        return redirect("login")

    return render(request, "accounts/patient_signup.html")


def doctor_signup_view(request):
    if request.method == "POST":
        username = request.POST.get("username").strip()
        password = request.POST.get("password").strip()
        confirm = request.POST.get("confirm_password").strip()

        full_name = request.POST.get("full_name").strip()
        specialization = request.POST.get("specialization").strip()
        phone = request.POST.get("phone").strip()

        if password != confirm:
            messages.error(request, "Passwords do not match.")
            return redirect("doctor_signup")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken.")
            return redirect("doctor_signup")

        user = User.objects.create_user(
            username=username,
            password=password,
            first_name=full_name,
        )

        Doctor.objects.create(
            user=user,
            specialization=specialization,
            phone=phone,
        )

        messages.success(request, "Doctor account created. Please login.")
        return redirect("login")

    return render(request, "accounts/doctor_signup.html")


@login_required
def admin_dashboard(request):
    if not request.user.is_superuser:
        return redirect("home")

    context = {
        "total_users": User.objects.count(),
        "total_doctors": Doctor.objects.count(),
        "total_patients": Patient.objects.count(),
        "total_appointments": Appointment.objects.count(),
    }
    return render(request, "accounts/admin_dashboard.html", context)


@login_required
def admin_doctor_list(request):
    if not request.user.is_superuser:
        return redirect("home")

    doctors = Doctor.objects.select_related("user").all()
    return render(request, "accounts/manage_doctors.html", {"doctors": doctors})


@login_required
def admin_patient_list(request):
    if not request.user.is_superuser:
        return redirect("home")

    patients = Patient.objects.select_related("user").all()
    return render(request, "accounts/manage_patients.html", {"patients": patients})


@login_required
def admin_appointment_list(request):
    if not request.user.is_superuser:
        return redirect("home")

    appointments = Appointment.objects.select_related("doctor__user", "patient__user").order_by(
        "-date", "-time"
    )
    return render(
        request,
        "accounts/manage_appointments.html",
        {"appointments": appointments},
    )
