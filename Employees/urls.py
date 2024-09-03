from django.contrib import admin
from django.urls import path
from Employees.views import Employee,listEmployees,UpdateEmployee,DestroyEmployee,RetrieveEmployee


urlpatterns = [
    path('employee/',Employee.as_view(),name="employee"),
    path('employee-list/',listEmployees.as_view(),name="list_employees"),
    path('update-employee/<int:pk>',UpdateEmployee.as_view(),name="update-employee"),
    path('retrieve-employee/<int:pk>',RetrieveEmployee.as_view(),name="retrieve-employee"),
    path('delete-employee/<int:pk>',DestroyEmployee.as_view(),name="destroy-employee"),
    

   
    
]







