from django.urls import path
from Companys.views import Create_company,Company_list,ManageCompany


urlpatterns = [
    path('employee/',Create_company.as_view(),name="employee"),
    path('employee-list/',Company_list.as_view(),name="list_employees"),
    path('manageemployee/<int:pk>',ManageCompany.as_view(),name="update_employee"),
    
]

