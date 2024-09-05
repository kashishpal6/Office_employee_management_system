from .models import contact
from .serializers import contactSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny,IsAuthenticated


class contact_us(generics.CreateAPIView):
   queryset=contact.objects.all()
   serializer_class=contactSerializer
   permission_classes= [AllowAny]

class list_contact_us(generics.ListAPIView):
   queryset=contact.objects.all()
   serializer_class=contactSerializer
   permission_classes= [IsAuthenticated]



