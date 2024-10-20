from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from smartmedical.models import *
from django.contrib.auth.models import User
counter = 5
counter_val = counter - 1
# Create
def create_patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to a success page or do whatever you need to do
            return redirect('patient_list')  # Change 'success-page' to your actual success page URL
    else:
        form = PatientForm()
    return render(request, 'patient_form.html', {'form': form})


def create_prescription(request):
    if request.method == 'POST':
        form = PrescriptionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            print_hello()
            print(counter_val)
            return redirect('prescription_list')
    else:
        form = PrescriptionForm()
    return render(request, 'prescription_form.html', {'form': form})

# Create
def create_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('appointment_list')  # Redirect to appointment list view
    else:
        form = AppointmentForm()
    return render(request, 'appointment_form.html', {'form': form})

def create_exercise(request):
    if request.method == 'POST':
        form = ExerciseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('exercise_list')  # Redirect to exercise list view
    else:
        form = ExerciseForm()
    return render(request, 'smartmedexercise_form.html', {'form': form})

def create_medicine_consumed(request):
    if request.method == 'POST':
        form = MedicineConsumedForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('medicine_consumed_list')  # Redirect to medicine consumed list view
    else:
        form = MedicineConsumedForm()
    return render(request, 'medicine_consumed_form.html', {'form': form})

# Read
def patient_list(request):
    patients = Patient.objects.all()
    if counter_val == 0:
                send_email_refill()
    return render(request, 'patient_list.html', {'patients': patients})

def prescription_list(request):
    prescriptions = Prescription.objects.all()
    print_hello()
    if counter_val == 0:
                send_email_refill()
    return render(request, 'prescription_list.html', {'prescriptions': prescriptions})

def prescription_list_user(request):
    prescriptions = Prescription.objects.all()
    if counter_val == 0:
                send_email_refill()
    return render(request, 'prescription_list_user.html', {'prescriptions': prescriptions})


def appointment_list(request):
    appointments = Appointment.objects.all()
    return render(request, 'appointment_list.html', {'appointments': appointments})

def exercise_list(request):
    exercises = Exercise.objects.all()
    return render(request, 'smartmedexercise_list.html', {'exercises': exercises})


def medicine_consumed_list(request):
    send_email_refill()
    return render(request, 'medi.html')

# Update
def update_patient(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    if request.method == 'POST':
        form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            return redirect('patient_list')
    else:
        form = PatientForm(instance=patient)
    return render(request, 'patient_form.html', {'form': form})

def update_prescription(request, pk):
    prescription = get_object_or_404(Prescription, pk=pk)
    if request.method == 'POST':
        form = PrescriptionForm(request.POST, request.FILES, instance=prescription)
        if form.is_valid():
            form.save()
            return redirect('prescription_list')
    else:
        form = PrescriptionForm(instance=prescription)
    return render(request, 'prescription_form.html', {'form': form})

# Update
def update_appointment(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    if request.method == 'POST':
        form = AppointmentForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
            return redirect('appointment_list')
    else:
        form = AppointmentForm(instance=appointment)
    return render(request, 'appointment_form.html', {'form': form})

def update_exercise(request, pk):
    exercise = get_object_or_404(Exercise, pk=pk)
    if request.method == 'POST':
        form = ExerciseForm(request.POST, instance=exercise)
        if form.is_valid():
            form.save()
            return redirect('exercise_list')
    else:
        form = ExerciseForm(instance=exercise)
    return render(request, 'smartmedexercise_form.html', {'form': form})

def update_medicine_consumed(request, pk):
    medicine_consumed = get_object_or_404(MedicineConsumed, pk=pk)
    if request.method == 'POST':
        form = MedicineConsumedForm(request.POST, instance=medicine_consumed)
        if form.is_valid():
            form.save()
            return redirect('medicine_consumed_list')
    else:
        form = MedicineConsumedForm(instance=medicine_consumed)
    return render(request, 'medicine_consumed_form.html', {'form': form})

# Delete
def delete_patient(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    if request.method == 'POST':
        patient.delete()
        return redirect('patient_list')
    return render(request, 'patient_confirm_delete.html', {'object': patient})

def delete_prescription(request, pk):
    prescription = get_object_or_404(Prescription, pk=pk)
    if request.method == 'POST':
        prescription.delete()
        return redirect('prescription_list')
    return render(request, 'prescription_confirm_delete.html', {'object': prescription})

def delete_appointment(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    if request.method == 'POST':
        appointment.delete()
        return redirect('appointment_list')
    return render(request, 'appointment_confirm_delete.html', {'object': appointment})

def delete_exercise(request, pk):
    exercise = get_object_or_404(Exercise, pk=pk)
    if request.method == 'POST':
        exercise.delete()
        return redirect('exercise_list')
    return render(request, 'exercise_confirm_delete.html', {'object': exercise})

def delete_medicine_consumed(request, pk):
    medicine_consumed = get_object_or_404(MedicineConsumed, pk=pk)
    if request.method == 'POST':
        medicine_consumed.delete()
        return redirect('medicine_consumed_list')
    return render(request, 'medicine_consumed_confirm_delete.html', {'object': medicine_consumed})

from django.http import JsonResponse
from django.utils import timezone

from datetime import timedelta
from datetime import datetime, timedelta
from django.http import JsonResponse
from django.utils import timezone
from .models import Prescription

def get_prescriptions_matching_current_time(request):
    current_time = timezone.now().time()
    print("..............................", current_time)
    
    # Define a time window for matching prescriptions (e.g., 1 minute)
    time_window_start = (datetime.combine(datetime.today(), current_time) - timedelta(minutes=1)).time()
    time_window_end = (datetime.combine(datetime.today(), current_time) + timedelta(minutes=1)).time()
    
    # Filter prescriptions within the time window
    matching_prescriptions = Prescription.objects.filter(
        time_to_be_taken__gte=time_window_start,
        time_to_be_taken__lte=time_window_end
    )
    print("..............................", matching_prescriptions)
    
    # Serialize the matching prescriptions queryset into JSON
    prescriptions_data = list(matching_prescriptions.values())
    
    # Return the JSON response
    return JsonResponse(prescriptions_data, safe=False)

from django.core.mail import send_mail
from django.shortcuts import render
from .models import MedicineConsumed, Patient

def send_medication_reminder(request):
    # Retrieve all MedicineConsumed objects
    medicines_consumed = MedicineConsumed.objects.all()

    for medicine_consumed in medicines_consumed:
        # Retrieve associated Prescription and Patient information
        prescription = medicine_consumed.prescription
        patient = prescription.patient

        # Compose the email message
        subject = f"Medication Reminder for {patient.patient_name}"
        message = f"Dear {patient.caretaker},\n\nThis is a reminder that {patient.patient_name} has taken their medication at {medicine_consumed.time_taken}.\n\nPlease ensure that the patient follows the prescribed dosage.\n\nSincerely,\nYour Smart Medical System"
        sender_email = "rakshitahalaj@gmail.com"  # Change this to your sender email
        recipient_email = patient.caretaker_email

        # Send the email
        send_mail(subject, message, sender_email, [recipient_email])

    return redirect('dashboard')

from django.core.mail import EmailMessage
from django.conf import settings
from django.shortcuts import redirect

def send_email():
    try:
        receiver = "rakshitahalaj@gmail.com"
        subject = "Medication Status"
        message = "Patient has had the tablet"

        email = EmailMessage(
            subject=subject,
            body=message,
            from_email=settings.EMAIL_HOST_USER,
            to=[receiver],
        )
        email.send()

        return redirect('dashboard')  # Redirect to 'dashboard' after sending email
    except Exception as e:
        # Handle the exception, e.g., log the error or show an error message
        print(f"Error sending email: {e}")
        # You can return an HttpResponse or render a template with an error message
        return HttpResponse("Error sending email. Please try again later.")


def send_email_refill():
    try:
        receiver = "rakshitahalaj@gmail.com"
        subject = "Medication Refill Status"
        message = "Medicine needs refill"

        email = EmailMessage(
            subject=subject,
            body=message,
            from_email=settings.EMAIL_HOST_USER,
            to=[receiver],
        )
        email.send()

        return redirect('dashboard')  # Redirect to 'dashboard' after sending email
    except Exception as e:
        # Handle the exception, e.g., log the error or show an error message
        print(f"Error sending email: {e}")
        # You can return an HttpResponse or render a template with an error message
        return HttpResponse("Error sending email. Please try again later.")


from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
from .models import Patient, Prescription

def send_prescription_email(patient_id):
    try:
        # Fetch the patient and prescription details
        patient = Patient.objects.get(id=patient_id)
        prescriptions = Prescription.objects.filter(patient=patient)

        # Prepare the email content
        subject = 'Prescription Details'
        context = {
            'patient_name': patient.patient_name,
            'prescriptions': prescriptions,
        }
        html_message = render_to_string('email_template.html', context)
        plain_message = strip_tags(html_message)

        # Send email to caretaker
        send_mail(
            subject,
            plain_message,
            settings.EMAIL_HOST_USER,  # Sender's email
            [patient.caretaker_email],  # Caretaker's email
            html_message=html_message,
        )
        return True  # Email sent successfully
    except Exception as e:
        print(e)
        return False  # Failed to send email

from django.http import HttpResponse
from datetime import datetime

from .models import Prescription
import serial
import time

# Define the serial port and baud rate
serial_port = 'COM8'  # Change 'COMX' to your Arduino's serial port
baud_rate = 9600
def print_hello():
    if counter_val == 0:
                send_email_refill()
                print('R_E_S')
    # Assuming prescription_id is passed in the URL to identify the prescription
    try:
        prescription = Prescription.objects.get(pk=4)
    except Prescription.DoesNotExist:
        return HttpResponse("Prescription not found.", status=404)
    
    # Get the time to be taken from the prescription
    time_to_be_taken = prescription.time_to_be_taken
    print("2B",time_to_be_taken)
    # Get the current time
    current_time = datetime.now().time()
    print("CUR",current_time)
    # Compare the current time with the time to be taken
    if current_time.hour == time_to_be_taken.hour and current_time.minute == time_to_be_taken.minute:
        # Initialize the serial connection
        ser = serial.Serial(serial_port, baud_rate)
        print("Serial connection established")

        # Send a signal to start Arduino
        ser.write(b'Start')
        print("Signal sent to Arduino")

        # Close the serial connection
        ser.close()
    send_email()


