from django.urls import path
from .views import HomeView,PatientDetailView,patient_create_view,patient_delete_view,patient_update_view

app_name = 'patient'

urlpatterns = [
    path('',HomeView.as_view(),name = 'home'),
    path('detail/<int:pk>/',PatientDetailView.as_view(),name = 'detail'),
    path('create/',patient_create_view,name = 'create'),
    path('delete/<int:pk>/',patient_delete_view,name = 'delete'),
    path('update/<int:pk>/',patient_update_view,name = 'update')
]
