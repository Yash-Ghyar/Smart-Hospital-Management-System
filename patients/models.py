from django.db import models
from django.contrib.auth.models import User


class Patient(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="patient",
    )
    dob = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, blank=True)
    address = models.TextField(blank=True)
    blood_group = models.CharField(max_length=5, blank=True)
    phone = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.user.get_full_name() or self.user.username


class MedicalHistory(models.Model):
    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
        related_name="history",
    )
    test_name = models.CharField(max_length=100)
    test_value = models.CharField(max_length=100)
    test_date = models.DateField()
    remarks = models.TextField(blank=True)

    def __str__(self):
        return f"{self.patient} - {self.test_name} ({self.test_date})"
