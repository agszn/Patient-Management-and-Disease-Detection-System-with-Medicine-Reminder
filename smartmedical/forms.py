# forms.py
from django import forms
from .models import *
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.core.exceptions import ValidationError
import re
from django.forms.widgets import TimeInput

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['patient_name','patient_id', 'assosiated_doctor', 'doctor_email', 'caretaker', 'caretaker_email', 'caretaker_phone']

    def __init__(self, *args, **kwargs):
        super(PatientForm, self).__init__(*args, **kwargs)
        self.fields['patient_name'].widget = forms.Select(choices=self.get_patient_choices())

    def get_patient_choices(self):
        # Get non-admin registered users
        users = User.objects.filter(is_staff=False)
        # Extract patient names
        patient_names = [user.username for user in users]
        # Create choices list
        choices = [(name, name) for name in patient_names]
        return choices


class TimePicker(TimeInput):
    input_type = 'time'

class PrescriptionForm(forms.ModelForm):
    time_to_be_taken = forms.TimeField(widget=TimePicker)

    def __init__(self, *args, **kwargs):
        super(PrescriptionForm, self).__init__(*args, **kwargs)
        self.fields['patient'].queryset = Patient.objects.all()

    class Meta:
        model = Prescription
        fields = '__all__'

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = '__all__'
        widgets = {
            'appointment_date': forms.DateInput(attrs={'type': 'date'}),
            'appointment_time': forms.TimeInput(attrs={'type': 'time'}),
        }

class ExerciseForm(forms.ModelForm):
    class Meta:
        model = Exercise
        fields = '__all__'
        widgets = {
            'exercise_time': forms.TimeInput(attrs={'type': 'time'}),
        }
        
class MedicineConsumedForm(forms.ModelForm):
    class Meta:
        model = MedicineConsumed
        fields = '__all__'
