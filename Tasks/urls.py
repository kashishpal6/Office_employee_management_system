from django.urls import path
from Tasks.views import Create_Task,Task_list,Manage_tasks


urlpatterns = [
    
    path('Create_Task/',Create_Task.as_view(),name="Task"),
    path('Task_list/',Task_list.as_view(),name="Task_list"),
    path('manage_tasks/<int:pk>',Manage_tasks.as_view(),name="manage_tasks"),
    
]