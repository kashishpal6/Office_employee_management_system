from django.urls import path
from Contact_us.views import contact_us,list_contact_us


urlpatterns = [
   
    path('contact-us/',contact_us.as_view(),name="contact"),
    path('list-contact_us/',list_contact_us.as_view(),name="list_contact_us"),
]
