# projects/serializers.py

from rest_framework import serializers
from .models import Project, Repository, Tracker

class RepositorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Repository
        fields = '__all__'

class TrackerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tracker
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    repositories = RepositorySerializer(many=True, required=False)
    trackers = TrackerSerializer(many=True, required=False)

    class Meta:
        model = Project
        fields = '__all__'

    def create(self, validated_data):
        repositories_data = validated_data.pop('repositories', [])
        trackers_data = validated_data.pop('trackers', [])
        project = Project.objects.create(**validated_data)
        for repository_data in repositories_data:
            Repository.objects.create(project=project, **repository_data)
        for tracker_data in trackers_data:
            Tracker.objects.create(project=project, **tracker_data)
        return project

    def update(self, instance, validated_data):
        repositories_data = validated_data.pop('repositories', [])
        trackers_data = validated_data.pop('trackers', [])

        instance.name = validated_data.get('name', instance.name)
        instance.slug = validated_data.get('slug', instance.slug)
        instance.description = validated_data.get('description', instance.description)
        instance.language = validated_data.get('language', instance.language)
        instance.save()

        instance.repositories.all().delete()
        instance.trackers.all().delete()

        for repository_data in repositories_data:
            Repository.objects.create(project=instance, **repository_data)
        for tracker_data in trackers_data:
            Tracker.objects.create(project=instance, **tracker_data)

        return instance
