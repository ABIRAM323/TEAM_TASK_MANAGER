from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from .serializers import UserSerializer, ProjectSerializer, TaskSerializer
from projects.models import Project
from tasks.models import Task
from django.contrib.auth import get_user_model

User = get_user_model()

# Custom permission to ensure only admins can modify projects.
# Members should only be able to view them.
class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        # Allow any safe method (GET, HEAD, OPTIONS)
        if request.method in permissions.SAFE_METHODS:
            return True
        # Write permissions are only allowed to users with 'admin' role
        return request.user.is_authenticated and request.user.role == 'admin'


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAdminOrReadOnly]

    def get_queryset(self):
        user = self.request.user
        if user.role == 'admin':
            return Project.objects.filter(owner=user)
        return Project.objects.filter(members=user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.role == 'admin':
            return Task.objects.filter(project__owner=user)
        return Task.objects.filter(assignee=user)

    def perform_create(self, serializer):
        # Only admins can create tasks for their projects
        project = serializer.validated_data.get('project')
        if self.request.user.role == 'admin' and project.owner == self.request.user:
            serializer.save()
        else:
            raise permissions.PermissionDenied("Only project admins can create tasks.")
