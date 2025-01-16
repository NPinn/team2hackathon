from django.urls import path

from clinicians import views

urlpatterns = [
    path('', views.index, name='create_patient_sheet'),
    path('generate-discharge-note/', views.generate_discharge_note, name='generate_discharge_note')
]
