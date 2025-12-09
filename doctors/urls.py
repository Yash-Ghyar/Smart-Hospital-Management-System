from django.urls import path
from . import views

urlpatterns = [
    path("dashboard/", views.doctor_dashboard, name="doctor_dashboard"),
    path("profile/", views.doctor_profile_edit, name="doctor_profile"),
    path("add-slot/", views.add_slot, name="add_slot"),
]
