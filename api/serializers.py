from rest_framework import serializers
from django.contrib.auth import get_user_model
from projects.models import Project
from tasks.models import Task

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'role', 'bio', 'avatar']

class ProjectSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)
    members = UserSerializer(many=True, read_only=True)
    member_ids = serializers.PrimaryKeyRelatedField(
        many=True, write_only=True, queryset=User.objects.all(), source='members'
    )

    class Meta:
        model = Project
        fields = ['id', 'name', 'description', 'owner', 'members', 'member_ids', 'created_at', 'updated_at']

    def create(self, validated_data):
        members = validated_data.pop('members', [])
        project = Project.objects.create(**validated_data)
        project.members.set(members)
        return project

class TaskSerializer(serializers.ModelSerializer):
    project_name = serializers.ReadOnlyField(source='project.name')
    assignee_name = serializers.ReadOnlyField(source='assignee.username')

    class Meta:
        model = Task
        fields = [
            'id', 'title', 'description', 'project', 'project_name', 
            'assignee', 'assignee_name', 'status', 'priority', 
            'due_date', 'created_at', 'updated_at'
        ]
