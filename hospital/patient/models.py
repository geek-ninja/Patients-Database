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
    