from rest_framework import viewsets, permissions, generics
from .models import Category, Course
from .serializers import CategorySerializer, CourseSerializer

class CategoryView(viewsets.ViewSet, generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CourseView(viewsets.ViewSet, generics.ListAPIView):
    queryset = Course.objects.filter(active=True)
    serializer_class = CategorySerializer
