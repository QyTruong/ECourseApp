from rest_framework.serializers import ModelSerializer
from .models import Category, Course, Lesson

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'name', 'created_date', 'image', 'category']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        if instance.image:
            data['image'] = instance.image.url

        return data

class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['id', 'name', 'created_date']