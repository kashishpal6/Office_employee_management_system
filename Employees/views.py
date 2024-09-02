from django.shortcuts import render
from .models import Employees
from .serializers import employeesSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny,IsAuthenticated

class Employee(generics.CreateAPIView):
   queryset=Employees.objects.all()
   serializer_class=employeesSerializer
   permission_classes = [IsAuthenticated]
   

   
class listEmployees(generics.ListAPIView):
   queryset=Employees.objects.all()
   serializer_class=employeesSerializer
   permission_classes = [AllowAny] 

class ManageEmployee(generics.RetrieveUpdateDestroyAPIView):
   queryset=Employees.objects.all()
   serializer_class=employeesSerializer 
   permission_classes =[IsAuthenticated]


    



