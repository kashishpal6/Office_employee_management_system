from django.contrib import admin
from django.urls import path,include
from Employees.views import Employee,listEmployees,ManageEmployee
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('employee/',Employee.as_view(),name="employee"),
    path('employee-list/',listEmployees.as_view(),name="list_employees"),
    path('manageemployee/<int:pk>',ManageEmployee.as_view(),name="update_employee"),
    
]







