from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('projects.urls')),  # Include projects app URLs under /api/
    path('', RedirectView.as_view(url='/api/', permanent=True)),  # Redirect root to /api/
]