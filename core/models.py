from __future__ import unicode_literals

from django.db import models

from authentication.models import User


class Project(models.Model):
    name = models.CharField(max_length=55)
    users = models.ManyToManyField(User, through='ProjectUser')

    def __unicode__(self):
        return self.name


class ProjectUser(models.Model):
    project = models.ForeignKey(Project)
    user = models.ForeignKey(User)

    class Meta:
        unique_together = ('project', 'user')

    def __unicode__(self):
        return '{0} - {1}'.format(self.project, self.user)


class Task(models.Model):
    title = models.CharField(max_length=55)
    description = models.TextField(blank=True)
    due_date = models.DateField()
    user = models.ForeignKey(User)
    project = models.ForeignKey(Project)

    def __unicode__(self):
        return self.title





