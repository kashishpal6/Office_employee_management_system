from Companys.models import Company
from .serializers import CompanySerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny

class Company_info(generics.ListAPIView):
   queryset=Company.objects.all()
   serializer_class=CompanySerializer
   permission_classes = [AllowAny] 






