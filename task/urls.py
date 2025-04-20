from django.urls import path
from Tasks.views import Create_Task,Task_list,Update_tasks,Delete_tasks,Retrieve_tasks


urlpatterns = [
    
    path('Create_Task/',Create_Task.as_view(),name="Task"),
    path('Task_list/',Task_list.as_view(),name="Task_list"),
    path('update-tasks/<int:pk>/',Update_tasks.as_view(),name="update_tasks"),
    path('delete-tasks/<int:pk>/',Delete_tasks.as_view(),name="delete_tasks"),
    path('retrieve-tasks/<int:pk>/',Retrieve_tasks.as_view(),name="retrieve_tasks"),
    
]