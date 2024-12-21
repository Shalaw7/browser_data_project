from django.contrib import admin
from django.urls import path, include  # Import `include` for app-specific routes

urlpatterns = [
    path("admin/", admin.site.urls),
    path("collector/", include("data_collector.urls")),  # Include the routes for the data_collector app
]
