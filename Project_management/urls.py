from django.urls import path
from .views import List_ProjectManager,CreateProjectmanager,ManageprojectManager

urlpatterns = [
    path('CreateProjectmanager',CreateProjectmanager.as_view(), name='project_employees_create'),
    path('List_ProjectManager/<str:project_name>/', List_ProjectManager.as_view(), name='project_employees_list'),
    path('ManageprojectManager/<int:pk>',ManageprojectManager.as_view(),name="manage_projects"),
]



