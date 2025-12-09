from django.contrib import admin
from .models import Doctor, Availability


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ("user", "specialization", "phone", "experience_years")


@admin.register(Availability)
class AvailabilityAdmin(admin.ModelAdmin):
    list_display = ("doctor", "day", "start_time", "end_time", "is_active")
    list_filter = ("doctor", "day", "is_active")
