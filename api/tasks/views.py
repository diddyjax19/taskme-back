from rest_framework import viewsets
from .serializers import TaskCreationUpdationSerializer,TaskListSerializer,CreateUpdateSubTask
from .models import Task
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination

# Create your views here.
class TaskCreationUpdationView(viewsets.ModelViewSet):
    serializer_class = TaskCreationUpdationSerializer
    lookup_field = 'id'
    http_method_names = ['get','put','post','delete']
    queryset = Task.objects.all()

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["user"] = self.request.user
        return context

    def destroy(self, request, *args, **kwargs):
        if self.request.user.is_staff or self.request.user.is_lead:
            return super().destroy(request, *args, **kwargs)
        return Response({"error": "Cannot delete task"})

class ProjectTaskListView(APIView):
    def get(self,request,project_id,me=None):
        if me:
            queryset = Task.objects.filter(project__id=project_id,assignedTo=request.user,state__in=['NEW','IN PROGRESS'])
        else:
            queryset = Task.objects.filter(project__id=project_id)
        serializer = TaskListSerializer(queryset,many=True)
        return Response(serializer.data)
        

class CreateSubTaskView(APIView,PageNumberPagination):
    serializer_class = CreateUpdateSubTask
    page_size = 1
    page_size_query_param = 'page_size'
    max_page_size = 10000
    
    def get(self, request,task_id):
        try:
            task = Task.objects.get(id=task_id)
        except Task.DoesNotExist:
            return Response({"error": "Parent task not found"},status=status.HTTP_400_BAD_REQUEST)
        else:
            queryset = task.subtasks.all()
            queryset = self.paginate_queryset(queryset, request)
            serializer = CreateUpdateSubTask(queryset,many=True)
            ser = self.get_paginated_response(serializer.data)
            
        return Response(ser.data)


    def post(self,request,task_id):
        try:
            task = Task.objects.get(id=task_id)
        except Task.DoesNotExist:
            return Response({"error": "Parent task not found"},status=status.HTTP_400_BAD_REQUEST)
        serializer = CreateUpdateSubTask(data=request.data,context={'user': request.user,'task': task})
        if (serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
