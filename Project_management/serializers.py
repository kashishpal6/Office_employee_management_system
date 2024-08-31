from rest_framework import serializers
from .models import Project_manager

class Project_managementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project_manager
        fields = ['name','project']