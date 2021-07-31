[![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://forthebadge.com)

# Patients-Database

<h2>Patient Datababe Website made using Django</h2><br>
<p>Here you can upload data of the patient and update the data and delete and view of details of the patients</p>

<p>hope you have installed django or else you can follow the command</p><br>
python -m pip install Django
<br>
<h3>Create the project</h3>
django-admin startproject hospital
<br>
<p>change the directory to the new project folder created</p>
<p>Then create the app for the project</p>
python3 manage.py startapp patient
<br>
<br>
<p>For quick overview of the project you can copy and overwrite the files and folder from the repo to the respective files of django that you have created</p>
<h3>How to run the django server</h3>
<p>now run the following commands</p>
python3 manage.py makemigrations 
python3 manage.py migrate <br> 
python manage.py runserver <br> 

<h2>Import CodeSnippents</h2>

<p>forms.py</p>

```python
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
    
```
<p>models.py</p>

```python
from django.db import models
from django.urls import reverse

class Patient(models.Model):
    GENDER_CHOICES = [
        ('Male','Male'),
        ('Female','Female'),
    ]
    
    First_Name = models.CharField(max_length  = 120)
    Last_Name = models.CharField(max_length = 120)
    Gender = models.CharField(max_length = 10, choices = GENDER_CHOICES)
    Age = models.IntegerField()
    Disease = models.TextField()
    Doctor_name = models.CharField(max_length = 200)
    Doctor_fees = models.DecimalField(decimal_places=2,max_digits=100000,default = 500.00)
    Starting_data_of_meds = models.DateTimeField(null = True,blank = True)
    Image = models.FileField(upload_to='images/',default = '')
    
    def __str__(self):
        return self.First_Name
    def get_absolute_url(self):
        return reverse("patient:detail", kwargs={"pk": self.pk})
    
```

