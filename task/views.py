from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework import status
from .serializers import TaskSerializer
from .models import Tasks
from rest_framework import generics
from rest_framework.permissions import AllowAny,IsAuthenticated

@api_view(['POST'])
def create_task(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Task_list(generics.ListAPIView):
   queryset=Tasks.objects.all()
   serializer_class=TaskSerializer
   permission_classes= [AllowAny]

class Update_tasks(generics.UpdateAPIView):
   queryset=Tasks.objects.all()
   serializer_class=TaskSerializer 
   permission_classes =[IsAuthenticated]

class Delete_tasks(generics.DestroyAPIView):
   queryset=Tasks.objects.all()
   serializer_class=TaskSerializer 
   permission_classes =[IsAuthenticated]

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_tasks(request):
    tasks = Tasks.objects.filter(employee=request.user)
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)

