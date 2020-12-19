from django.urls import path
from . import views

urlpatterns = [
    path('', views.Search, name="Search"), 
    path('getAll/', views.getAll, name="getAll"),  
    path('customSearch/', views.customSearch, name="customSearch"),
    path('getModelsFields/', views.getModelsFields, name="getModelsFields"),    
 ]
 