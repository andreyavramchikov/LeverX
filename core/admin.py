from django.contrib import admin

from .models import Project, Task


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    pass


@admin.register(Task)
class ProjectAdmin(admin.ModelAdmin):
    pass
