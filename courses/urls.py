from django.urls import path, re_path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('categories', views.CategoryView, basename="category")
router.register('courses', views.CourseView, basename="course")
router.register('lessons', views.LessonView, basename="lesson")
router.register('users', views.UserView, basename="user")
router.register('comments', views.CommentView, basename="comment")

urlpatterns = [
    path('', include(router.urls)),
]