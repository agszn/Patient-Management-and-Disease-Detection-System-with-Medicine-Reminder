from unicodedata import name
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    # URLs for Patient model
    path('patient/create/', views.create_patient, name='create_patient'),
    path('patient/<int:pk>/update/', views.update_patient, name='update_patient'),
    path('patient/<int:pk>/delete/', views.delete_patient, name='delete_patient'),
    path('patient/', views.patient_list, name='patient_list'),

    # URLs for Prescription model
    path('prescription/create/', views.create_prescription, name='create_prescription'),
    path('prescription/<int:pk>/update/', views.update_prescription, name='update_prescription'),
    path('prescription/<int:pk>/delete/', views.delete_prescription, name='delete_prescription'),
    path('prescription/', views.prescription_list, name='prescription_list'),
    path('prescription_list_user/', views.prescription_list_user, name='prescription_list_user'),


    # URLs for Appointment model
    path('appointment/create/', views.create_appointment, name='create_appointment'),
    path('appointment/<int:pk>/update/', views.update_appointment, name='update_appointment'),
    path('appointment/<int:pk>/delete/', views.delete_appointment, name='delete_appointment'),
    path('appointment/', views.appointment_list, name='appointment_list'),

    # URLs for Exercise model
    path('exercise/create/', views.create_exercise, name='smartmedcreate_exercise'),
    path('exercise/<int:pk>/update/', views.update_exercise, name='smartmedupdate_exercise'),
    path('exercise/<int:pk>/delete/', views.delete_exercise, name='smartmeddelete_exercise'),
    path('exercise/', views.exercise_list, name='smartmedexercise_list'),

    # URLs for MedicineConsumed model
    path('medicine_consumed/create/', views.create_medicine_consumed, name='create_medicine_consumed'),
    path('medicine_consumed/<int:pk>/update/', views.update_medicine_consumed, name='update_medicine_consumed'),
    path('medicine_consumed/<int:pk>/delete/', views.delete_medicine_consumed, name='delete_medicine_consumed'),
    path('medicine_consumed/', views.medicine_consumed_list, name='medicine_consumed_list'),

    path('get_prescriptions_matching_current_time/',views.get_prescriptions_matching_current_time,name="get_prescriptions_matching_current_time"),
    path('send_medication_reminder/',views.send_medication_reminder,name="send_medication_reminder"),
    path('send_email/', views.send_email, name='send_email'),


]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
