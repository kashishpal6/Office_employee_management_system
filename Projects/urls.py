from django.urls import path
from Projects.views import Listprojects,create_projects,Updateprojects,Deleteprojects,Retrieveprojects


urlpatterns = [
   
    path('Listprojects/',Listprojects.as_view(),name="list_projects"),
    path('create_projects/',create_projects.as_view(),name="create_projects"),
    path('update-projects/<int:pk>/',Updateprojects.as_view(),name="update-projects"),
    path('delete-projects/<int:pk>/',Deleteprojects.as_view(),name="delete-projects"),
    path('retrieve-projects/<int:pk>/',Retrieveprojects.as_view(),name="retrieve-projects"),
]
