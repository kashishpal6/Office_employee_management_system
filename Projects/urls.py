from django.urls import path
from Projects.views import Listprojects,create_projects,Manageprojects


urlpatterns = [
   
    path('Listprojects/',Listprojects.as_view(),name="list_projects"),
    path('create_projects/',create_projects.as_view(),name="create_projects"),
    path('manageprojects/<int:pk>',Manageprojects.as_view(),name="manage_projects"),
]
