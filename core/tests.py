from datetime import datetime
from django.core.urlresolvers import reverse

from rest_framework import status
from rest_framework.test import APITestCase

from core.models import Project, Task
from authentication.models import User


class PageResponseTests(APITestCase):

    @classmethod
    def setUpTestData(cls):
        cls.INSTANCE_PK = 1
        cls.project = Project.objects.create(name='name')
        cls.user = User.objects.create_user(email='email@gmail.com', password='andreyPasan1')
        cls.task = Task.objects.create(title='Title', description='Description',
                                       user=cls.user, project=cls.project, due_date=datetime.now().date())

    def test_non_parameter_urls(self):
        urls = ('projects', 'tasks', 'users', 'project-users')
        for url in urls:
            url = reverse(url)
            response = self.client.get(url)
            self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_parameters_urls(self):
        urls = ('project', 'task', 'user')
        for url in urls:
            url = reverse(url, kwargs={'pk': self.INSTANCE_PK})
            response = self.client.get(url)
            self.assertEqual(response.status_code, status.HTTP_200_OK)