from django.urls import path
from . import views

urlpatterns = [
    path("dashboard/", views.patient_dashboard, name="patient_dashboard"),
    path("profile/", views.patient_profile_edit, name="patient_profile"),
    path("book/", views.book_appointment, name="book_appointment"),
]
