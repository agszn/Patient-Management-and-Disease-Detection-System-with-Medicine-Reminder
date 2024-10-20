# models.py
from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.db import models

class Patient(models.Model):
    patient_name = models.CharField(max_length=100)
    patient_id = models.IntegerField(default=0)  
    assosiated_doctor = models.CharField(max_length=100)
    doctor_email = models.EmailField(max_length=100)
    caretaker = models.CharField(max_length=100)
    caretaker_email = models.EmailField(max_length=100,default="rakshitahalaj@gmail.com")
    caretaker_phone = models.CharField(max_length=12)  

    def __str__(self):
        return self.patient_name

class Prescription(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, default=1)
    report_document = models.FileField(upload_to='prescription_reports/')
    medicine_name = models.CharField(max_length=200)
    time_to_be_taken = models.TimeField()
    number_of_days = models.IntegerField()
    meals_choices = (
        ('before', 'Before meals'),
        ('after', 'After meals'),
    ) 
    before_or_after_meals = models.CharField(max_length=10, choices=meals_choices)
    instructions = models.TextField(blank=True, max_length=500)

    def __str__(self):
        return f"Prescription for {self.patient.patient_name} - {self.medicine_name}"


class Appointment(models.Model):
    appointment_title = models.CharField(max_length=200)
    appointment_description = models.TextField()
    appointment_date = models.DateField()
    appointment_time = models.TimeField()

class Exercise(models.Model):
    prescription = models.OneToOneField(Prescription, on_delete=models.CASCADE)
    exercise_name = models.CharField(max_length=200)
    exercise_type_choices = (
        ('aerobic', 'Aerobic'),
        ('strength', 'Strength'),
        ('flexibility', 'Flexibility'),
    )
    exercise_type = models.CharField(max_length=20, choices=exercise_type_choices)
    exercise_time = models.TimeField()
    discription = models.TextField()

class MedicineConsumed(models.Model):
    prescription = models.ForeignKey(Prescription, on_delete=models.CASCADE,null=True, blank=True)
    caretaker_email = models.EmailField(max_length=100,default="rakshitahalaj@gmail.com")
    time_taken = models.TimeField()

    def __str__(self):
        return f"{self.prescription.patient.patient_name}'s {self.prescription.medicine.name} taken at {self.time_taken}"

