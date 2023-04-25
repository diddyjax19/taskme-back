from rest_framework import viewsets
from .serializers import ProjectSerializer
from .models import Project
from rest_framework.parsers import FormParser, MultiPartParser, JSONParser
from rest_framework import status
from rest_framework.response import Response

# Create your views here.
class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()
    lookup_field = 'id'
    parser_classes = [FormParser, MultiPartParser, JSONParser]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['user'] = self.request.user
        return context
    
    def destroy(self, request, *args, **kwargs):
        if request.user.is_staff:
            return super().destroy(request, *args, **kwargs)
        return Response({"error": "You cannot delete any project"},status=status.HTTP_400_BAD_REQUEST)