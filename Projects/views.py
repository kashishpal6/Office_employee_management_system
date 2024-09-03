from .models import Project
from .serializers import projectsSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny,IsAuthenticated


class create_projects(generics.CreateAPIView):
   queryset=Project.objects.all()
   serializer_class=projectsSerializer
   permission_classes= [IsAuthenticated]

class Listprojects(generics.ListAPIView):
   queryset=Project.objects.all()
   serializer_class=projectsSerializer
   permission_classes= [AllowAny]

class Updateprojects(generics.UpdateAPIView):
   queryset=Project.objects.all()
   serializer_class=projectsSerializer 
   permission_classes =[IsAuthenticated]

class Deleteprojects(generics.DestroyAPIView):
   queryset=Project.objects.all()
   serializer_class=projectsSerializer 
   permission_classes =[IsAuthenticated]

class Retrieveprojects(generics.RetrieveAPIView):
   queryset=Project.objects.all()
   serializer_class=projectsSerializer 
   permission_classes =[AllowAny]


