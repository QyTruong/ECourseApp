from django.urls import path, re_path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('category', views.CategoryView, basename="category")
router.register('course', views.CourseView, basename="course")

urlpatterns = [
    path('', include(router.urls)),
]