from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import PatientSheetForm


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
    medical_clearance = request.POST.get('medical_clearance', '')

    # Example logic to generate a discharge note
    # Replace this with your actual logic (e.g., AI, rules-based, etc.)
    discharge_note = f"Discharge Note based on Medical Clearance:\n\n{medical_clearance}"

    return JsonResponse({'discharge_note': discharge_note})