from django.urls import path
from Companys.views import Create_company,Company_list,UpdateCompany,DeleteCompany,RetrieveCompany


urlpatterns = [
    path('company/',Create_company.as_view(),name="comapny"),
    path('company-list/',Company_list.as_view(),name="company-list"),
    path('retrieve-company/<int:pk>/',RetrieveCompany.as_view(),name="retrieve-company"),
    path('update-company/<int:pk>/',UpdateCompany.as_view(),name="update-company"),
    path('delete-company/<int:pk>/',DeleteCompany.as_view(),name="delete-company"),

    
]

