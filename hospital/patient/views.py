from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic import ListView,DetailView
from .models import Patient
from .forms import PatientForm ,RawPatientForm
import datetime

class HomeView(ListView):
    model = Patient
    template_name = "patient/home.html"

class PatientDetailView(DetailView):
    model = Patient
    template_name = "patient/detail.html"
    
def patient_create_view(request):
    
    
    med_form = RawPatientForm()
    if request.method == "POST" or None:
        med_form = RawPatientForm(request.POST or None , request.FILES or None)
        if med_form.is_valid():
            Patient.objects.create(**med_form.cleaned_data)
            return redirect('../')
    context = {'form':med_form}
    
    
    
    #     first_name = request.POST.get('first_name')
    #     last_name = request.POST.get('last_name')
    #     gender = request.POST.get('gender')
    #     problem = request.POST.get('disease')
    #     doc_name = request.POST.get('doctor_name')
    #     doc_fees = request.POST.get('doctor_fees')
    #     date = request.POST.get('date')
    #     print(date)
        
    #     Patient.objects.create(First_Name = first_name,Last_Name = last_name,Gender = gender,Disease = problem,Doctor_name = doc_name,Doctor_fees = doc_fees,Starting_data_of_meds = date)
    # else:
    #     print('null')
    
    # med_form = PatientForm(request.POST or None)
    # if med_form.is_valid():
    #     med_form.save()
    # context = {
    #     'form' : med_form
    # }
    return render(request,"patient/create.html",context)

def patient_delete_view(request,pk):
    patient = get_object_or_404(Patient,pk = pk)
    if request.method == "POST":
        patient.delete()
        return redirect('../../')
    context = {
        "patient":patient
    }
    return render(request,"patient/delete.html",context)

def patient_update_view(request,pk):
    patient = get_object_or_404(Patient,pk = pk)
    med_form = PatientForm(request.POST or None,request.FILES or None , instance = patient)
    if med_form.is_valid():
        med_form.save()
        return redirect('../../')
    context = {
        'form':med_form
    }
    return render(request,"patient/update.html",context)