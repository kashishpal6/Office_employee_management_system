from rest_framework import serializers
from .models import Project


class projectsSerializer(serializers.ModelSerializer):

   class Meta:
      model=Project
      fields=['Project_name','Project_image','Description','Manager','Start_date','Deadline','Technology']