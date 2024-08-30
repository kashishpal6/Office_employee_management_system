from rest_framework import serializers
from .models import Employees




class employeesSerializer(serializers.ModelSerializer):

   class Meta:
      model=Employees
      fields=['Employee_name','phone_number','Profile_image','email','Joining_date','Skills','Designation']