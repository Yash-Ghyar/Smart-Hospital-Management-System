from django.contrib import admin
from .models import Patient, MedicalHistory


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ("user", "phone", "blood_group", "gender")


@admin.register(MedicalHistory)
class MedicalHistoryAdmin(admin.ModelAdmin):
    list_display = ("patient", "test_name", "test_date", "test_value")
    list_filter = ("test_date",)
