from rest_framework import generics
from .models import Project_manager
from .serializers import Project_managementSerializer
from rest_framework.permissions import AllowAny,IsAuthenticated

class List_ProjectManager(generics.ListAPIView):
    serializer_class = Project_managementSerializer

    def get_queryset(self):
        project_name = self.kwargs['project_name']
        return Project_manager.objects.filter(project__Project_name=project_name)
    

class CreateProjectmanager(generics.CreateAPIView):
    queryset = Project_manager.objects.all()  
    serializer_class = Project_managementSerializer
    permission_classes = [IsAuthenticated]

class ManageprojectManager(generics.RetrieveUpdateDestroyAPIView):
   queryset=Project_manager.objects.all()
   serializer_class=Project_managementSerializer
   permission_classes =[IsAuthenticated]

class List_EmployeeManager(generics.ListAPIView):
    serializer_class = Project_managementSerializer

    def get_queryset(self):
        Employee_id = self.kwargs['Employee_id']
        return Project_manager.objects.filter(name__Employee_id=Employee_id)
