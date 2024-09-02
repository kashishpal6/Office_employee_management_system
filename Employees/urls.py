from django.contrib import admin
from django.urls import path,include
from Employees.views import Employee,listEmployees,ManageEmployee


urlpatterns = [
    path('employee/',Employee.as_view(),name="employee"),
    path('employee-list/',listEmployees.as_view(),name="list_employees"),
    path('manageemployee/<int:pk>',ManageEmployee.as_view(),name="update_employee"),
   
    
]







