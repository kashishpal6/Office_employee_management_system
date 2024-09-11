from django.urls import path
from Companys.views import Company_info


urlpatterns = [
    path('company-info/',Company_info.as_view(),name="company-list"),
]

