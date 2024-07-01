from django.urls import path
from .views import ProjectListCreateView, ProjectRetrieveUpdateDestroyView, RepositoryListCreateView, RepositoryRetrieveUpdateDestroyView, TrackerListCreateView, TrackerRetrieveUpdateDestroyView, home

urlpatterns = [
    path('', home, name='home'),
    path('projects/', ProjectListCreateView.as_view(), name='project-list-create'),
    path('projects/<int:pk>/', ProjectRetrieveUpdateDestroyView.as_view(), name='project-detail'),
    path('repositories/', RepositoryListCreateView.as_view(), name='repository-list-create'),
    path('repositories/<int:pk>/', RepositoryRetrieveUpdateDestroyView.as_view(), name='repository-detail'),
    path('trackers/', TrackerListCreateView.as_view(), name='tracker-list-create'),
    path('trackers/<int:pk>/', TrackerRetrieveUpdateDestroyView.as_view(), name='tracker-detail'),
]
