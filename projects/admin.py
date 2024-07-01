from django.contrib import admin
from .models import Project, Repository, Tracker

admin.site.register(Project)
admin.site.register(Repository)
admin.site.register(Tracker)
