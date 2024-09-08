from .models import Employees
from .serializers import employeesSerializer
from rest_framework import generics,response,status
from rest_framework.permissions import AllowAny,IsAuthenticated
from Project_management.models import Project_manager
from Projects.serializers import projectsSerializer
from Projects.models import *
from Tasks.models import Tasks
from Tasks.serializers import TasksSerializer

class Employee(generics.CreateAPIView):
   queryset=Employees.objects.all()
   serializer_class=employeesSerializer
   permission_classes = [IsAuthenticated]
   

   
class listEmployees(generics.ListAPIView):
   queryset=Employees.objects.all()
   serializer_class=employeesSerializer
   permission_classes = [AllowAny] 

class UpdateEmployee(generics.UpdateAPIView):
   queryset=Employees.objects.all()
   serializer_class=employeesSerializer 
   permission_classes =[IsAuthenticated]

class DeleteEmployee(generics.DestroyAPIView):
   queryset=Employees.objects.all()
   serializer_class=employeesSerializer 
   permission_classes =[IsAuthenticated]

class RetrieveEmployee(generics.RetrieveAPIView):
    serializer_class = employeesSerializer
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        emp_data = Employees.objects.get(Employee_id=self.kwargs['pk'])
        project_managers = Project_manager.objects.filter(name__Employee_id=self.kwargs['pk'])
        emp_serialized = employeesSerializer(emp_data).data
        projects = [project_manager.project for project_manager in project_managers]
        project_serialized = projectsSerializer(projects, many=True).data
        tasks = Tasks.objects.filter(Assigned_to__name=emp_data)
        tasks_serialized = TasksSerializer(tasks, many=True).data

        data = {
            'employee_data': emp_serialized,
            'projects': project_serialized,
            'tasks': tasks_serialized
         }
        return response.Response(data=data, status=status.HTTP_200_OK)


   


        

        