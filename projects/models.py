import uuid
from django.db import models

class Project(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    language = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Repository(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    project = models.ForeignKey(Project, related_name='repositories', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    url = models.URLField()
    type = models.CharField(max_length=10, choices=[('GitHub', 'GitHub'), ('GitLab', 'GitLab'), ('Bitbucket', 'Bitbucket')])
    email = models.EmailField()
    token = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Tracker(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    project = models.ForeignKey(Project, related_name='trackers', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    url = models.URLField()
    type = models.CharField(max_length=10, choices=[('GitHub', 'GitHub'), ('GitLab', 'GitLab'), ('Jira', 'Jira')])
    email = models.EmailField()
    token = models.CharField(max_length=100)

    def __str__(self):
        return self.title
