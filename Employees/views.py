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

class UpdateEmployee(generics.UpdateAPIView):
   queryset=Employees.objects.all()
   serializer_class=employeesSerializer 
   permission_classes =[IsAuthenticated]

class RetrieveEmployee(generics.RetrieveAPIView):
   queryset=Employees.objects.all()
   serializer_class=employeesSerializer 
   permission_classes =[AllowAny]

class DestroyEmployee(generics.DestroyAPIView):
   queryset=Employees.objects.all()
   serializer_class=employeesSerializer 
   permission_classes =[IsAuthenticated]


    



