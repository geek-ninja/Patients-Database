from django import forms
from .models import Patient
import datetime

class DateInput(forms.DateInput):
    input_type = 'date'

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = [
            'First_Name',
            'Last_Name',
            'Gender',
            'Age',
            'Disease',
            'Doctor_name',
            'Doctor_fees',
            'Starting_data_of_meds',
            'Image'
        ]
        
class RawPatientForm(forms.Form):
    
    GENDER_CHOICES = [
        ('Male','Male'),
        ('Female','Female'),
    ]
    First_Name = forms.CharField(widget = forms.TextInput(attrs= {'placeholder': 'Enter First Name'}))
    Last_Name = forms.CharField(widget = forms.TextInput(attrs= {'placeholder': 'Enter Last Name'}))
    Gender = forms.ChoiceField(choices=GENDER_CHOICES)
    Age = forms.IntegerField(widget = forms.NumberInput(attrs={'placeholder':'Enter your Age'}))
    Disease = forms.CharField(widget = forms.Textarea(attrs={'rows': 4 , 'cols': 50,'placeholder':'Enter your Problems / Disease'}))
    Doctor_name = forms.CharField(widget = forms.TextInput(attrs={'placeholder': 'Enter your Doctor Name'}))
    Doctor_fees = forms.DecimalField(initial = 500.00)
    Starting_data_of_meds = forms.DateField(input_formats = ['%Y-%m-%d'],widget = DateInput)
    Image = forms.FileField()