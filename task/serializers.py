from rest_framework import serializers
from .models import Tasks 
class TaskSerializer(serializers.ModelSerializer):

   class Meta:
      model=Tasks
      fields="__all__"

   def validate_task(self, value):
      if len(value.strip())<3:
         raise serializers.ValidationError("Task name must be at keast 3 characters")
      return value