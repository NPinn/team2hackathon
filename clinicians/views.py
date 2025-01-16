from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from clinicians.forms import PatientSheetForm
from clinicians.logic import generate_discharge_note_from_medical_clerking
from embedding.chroma import ChromaDB

db = ChromaDB()


def index(request):
    if request.method == 'POST':
        form = PatientSheetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_page')  # Redirect to a success page
    else:
        form = PatientSheetForm()
    return render(request, 'patient_sheet.html', {'form': form})


@csrf_exempt  # Temporarily disable CSRF for testing (use proper CSRF handling in production)
@require_POST
def generate_discharge_note(request):
    medical_clerking = request.POST.get('medical_clerking', '')
    discharge_note = generate_discharge_note_from_medical_clerking(medical_clerking, db)

    return JsonResponse({'discharge_note': discharge_note})
