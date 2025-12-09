from django import forms
from .models import Patient


class PatientProfileForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ["dob", "gender", "address", "blood_group", "phone"]
        widgets = {
            "dob": forms.DateInput(attrs={"type": "date", "class": "form-control"}),
            "gender": forms.Select(
                choices=[
                    ("Male", "Male"),
                    ("Female", "Female"),
                    ("Other", "Other"),
                ],
                attrs={"class": "form-select"},
            ),
            "address": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
            "blood_group": forms.TextInput(attrs={"class": "form-control"}),
            "phone": forms.TextInput(attrs={"class": "form-control"}),
        }
