from django.shortcuts import render
from Companys.models import Company
from .serializers import CompanySerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny,IsAuthenticated

class Create_company(generics.CreateAPIView):
   queryset=Company.objects.all()
   serializer_class=CompanySerializer
   permission_classes = [IsAuthenticated]
   
class Company_list(generics.ListAPIView):
   queryset=Company.objects.all()
   serializer_class=CompanySerializer
   permission_classes = [AllowAny] 

class UpdateCompany(generics.UpdateAPIView):
   queryset=Company.objects.all()
   serializer_class=CompanySerializer 
   permission_classes =[IsAuthenticated]

class DeleteCompany(generics.DestroyAPIView):
   queryset=Company.objects.all()
   serializer_class=CompanySerializer 
   permission_classes =[IsAuthenticated]

class RetrieveCompany(generics.RetrieveAPIView):
   queryset=Company.objects.all()
   serializer_class=CompanySerializer 
   permission_classes =[AllowAny]


