from django.urls import path
from . import admin_views

urlpatterns = [
    path("manage-doctors/", admin_views.manage_doctors, name="manage_doctors"),
    path("manage-patients/", admin_views.manage_patients, name="manage_patients"),
    path("manage-appointments/", admin_views.manage_appointments, name="manage_appointments"),
]
