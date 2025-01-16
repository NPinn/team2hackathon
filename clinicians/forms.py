from django import forms


class PatientSheetForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    patient_id = forms.CharField(max_length=50)
    medical_clearance = forms.CharField(widget=forms.Textarea)
    discharge_note = forms.CharField(widget=forms.Textarea)
    feedback_rating = forms.IntegerField(min_value=1, max_value=5)