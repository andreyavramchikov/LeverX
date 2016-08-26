from rest_framework import serializers

from .models import Project, Task, ProjectUser


class ProjectUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectUser


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
