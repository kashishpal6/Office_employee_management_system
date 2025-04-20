from .models import Project
from .serializers import projectsSerializer
from rest_framework import generics,response,status
from rest_framework.permissions import AllowAny,IsAuthenticated
from Project_management.models import Project_manager
from Employees.models import Employees
from Employees.serializers import employeesSerializer

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
   serializer_class=projectsSerializer 
   permission_classes =[AllowAny]
   def get(self, request, *args, **kwargs):
      project = Project.objects.get(id=self.kwargs['pk'])
      project_serialized = projectsSerializer(project).data
      project_serialized['Project_image']=f"{'http://127.0.0.1:8000/'}{project_serialized['Project_image']}"
      project_manager = Project_manager.objects.filter(project=project)
      project_manager_ids = [pm.name.Employee_id for pm in project_manager]
      employees_data = Employees.objects.filter(Employee_id__in=project_manager_ids)
      employees_serialized = employeesSerializer(employees_data, many=True).data
      employees_info = [
            {
                'Emp_id': employee['Employee_id'],
                'name': employee['Employee_name']
            }
            for employee in employees_serialized
        ]

      data = {
            'project': project_serialized,
            'Team_members': employees_info
        }
      return response.Response(data=data, status=status.HTTP_200_OK)
     
   




