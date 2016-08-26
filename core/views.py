from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from authentication.models import User
from authentication.serializer import UserSerializer

from .serializer import ProjectSerializer, TaskSerializer, ProjectUsersSerializer
from .models import Project, Task, ProjectUser
from .permission import ManagerPermissions


class ProjectListView(ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = (ManagerPermissions,)


class ProjectView(RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = (ManagerPermissions,)


class TaskListView(ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (ManagerPermissions,)


class TaskView(RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (ManagerPermissions,)


class UserListView(ListCreateAPIView):
    queryset = User.objects.filter(user_type=User.DEVELOPER)
    serializer_class = UserSerializer
    permission_classes = (ManagerPermissions,)


class UserView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.filter(user_type=User.DEVELOPER)
    serializer_class = UserSerializer
    permission_classes = (ManagerPermissions,)


class ProjectUsersView(ListCreateAPIView):
    queryset = ProjectUser.objects.all()
    serializer_class = ProjectUsersSerializer
    permission_classes = (ManagerPermissions,)


