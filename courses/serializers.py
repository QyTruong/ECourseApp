from rest_framework.serializers import ModelSerializer
from .models import Category, Course

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'name', 'created_date', 'image']

