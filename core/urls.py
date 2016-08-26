from django.conf.urls import url

from .views import ProjectListView, ProjectView, TaskListView, \
    TaskView, UserView, UserListView, ProjectUsersView


urlpatterns = [
    url(r'^api/v1/project/$', ProjectListView.as_view(), name='projects'),
    url(r'^api/v1/project/(?P<pk>[0-9]+)/$', ProjectView.as_view(), name='project'),
    url(r'^api/v1/task/$', TaskListView.as_view(), name='tasks'),
    url(r'^api/v1/task/(?P<pk>[0-9]+)/$', TaskView.as_view(), name='task'),
    url(r'^api/v1/user/$', UserListView.as_view(), name='users'),
    url(r'^api/v1/user/(?P<pk>[0-9]+)/$', UserView.as_view(), name='user'),

    # url for m2m between project and user models
    url(r'^api/v1/project-users/$', ProjectUsersView.as_view(), name='project-users'),

]
