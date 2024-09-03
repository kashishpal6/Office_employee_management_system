from .models import Tasks
from .serializers import TasksSerializer
from  rest_framework import generics
from rest_framework.permissions import AllowAny,IsAuthenticated

class Create_Task(generics.CreateAPIView):
   queryset=Tasks.objects.all()
   serializer_class=TasksSerializer
   permission_classes= [IsAuthenticated]

class Task_list(generics.ListAPIView):
   queryset=Tasks.objects.all()
   serializer_class=TasksSerializer
   permission_classes= [AllowAny]

class Update_tasks(generics.UpdateAPIView):
   queryset=Tasks.objects.all()
   serializer_class=TasksSerializer 
   permission_classes =[IsAuthenticated]

class Delete_tasks(generics.UpdateAPIView):
   queryset=Tasks.objects.all()
   serializer_class=TasksSerializer 
   permission_classes =[IsAuthenticated]

class Retrieve_tasks(generics.RetrieveAPIView):
   queryset=Tasks.objects.all()
   serializer_class=TasksSerializer 
   permission_classes =[AllowAny]

