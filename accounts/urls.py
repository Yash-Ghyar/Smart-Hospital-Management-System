from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),

    path("signup/patient/", views.patient_signup_view, name="patient_signup"),
    path("signup/doctor/", views.doctor_signup_view, name="doctor_signup"),

    path("dashboard/admin/", views.admin_dashboard, name="admin_dashboard"),
    path("dashboard/admin/doctors/", views.admin_doctor_list, name="admin_doctors"),
    path("dashboard/admin/patients/", views.admin_patient_list, name="admin_patients"),
    path("dashboard/admin/appointments/", views.admin_appointment_list, name="admin_appointments"),
]
