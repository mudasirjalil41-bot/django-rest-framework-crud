"""
URL configuration for myproject project.
"""

from django.contrib import admin
from django.urls import path

# Sahi import: Kyunki aapki app ka naam 'project' hai
from project import views as project_views

urlpatterns = [
    path("admin/", admin.site.urls),
    # Aapka CRUD API endpoint jo 'project' app ke andar hai
    path("student/", project_views.student_api, name="student_list_create"),
    path(
        "student/<int:pk>/",
        project_views.student_api,
        name="student_detail_api",
    ),
]