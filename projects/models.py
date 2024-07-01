from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    language = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Repository(models.Model):
    GITHUB = 'GitHub'
    GITLAB = 'GitLab'
    BITBUCKET = 'Bitbucket'
    REPO_TYPE_CHOICES = [
        (GITHUB, 'GitHub'),
        (GITLAB, 'GitLab'),
        (BITBUCKET, 'Bitbucket'),
    ]

    project = models.ForeignKey(Project, related_name='repositories', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    url = models.URLField()
    type = models.CharField(max_length=10, choices=REPO_TYPE_CHOICES)
    email = models.EmailField()
    token = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Tracker(models.Model):
    GITHUB = 'GitHub'
    GITLAB = 'GitLab'
    JIRA = 'Jira'
    TRACKER_TYPE_CHOICES = [
        (GITHUB, 'GitHub'),
        (GITLAB, 'GitLab'),
        (JIRA, 'Jira'),
    ]

    project = models.ForeignKey(Project, related_name='trackers', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    url = models.URLField()
    type = models.CharField(max_length=10, choices=TRACKER_TYPE_CHOICES)
    email = models.EmailField()
    token = models.CharField(max_length=100)

    def __str__(self):
        return self.title