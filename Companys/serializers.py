from rest_framework import serializers
from .models import Company

class CompanySerializer(serializers.ModelSerializer):

   class Meta:
      model=Company
      fields=['Company_name','Location','Founding_date','Email','Description','Founder']