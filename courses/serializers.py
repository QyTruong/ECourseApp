from rest_framework.serializers import ModelSerializer
from .models import Category, Course, Lesson, Tag, User


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class ItemSerializer(ModelSerializer):
    def to_representation(self, instance):
        data = super().to_representation(instance)
        if instance.image:
            data['image'] = instance.image.url

        return data

class CourseSerializer(ItemSerializer):
    class Meta:
        model = Course
        fields = ['id', 'name', 'created_date', 'image', 'category']

class TagSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']

class LessonSerializer(ItemSerializer):
    class Meta:
        model = Lesson
        fields = ['id', 'name', 'image', 'created_date']

class LessonDetailsSerializer(LessonSerializer):
    tags = TagSerializer(many=True)

    class Meta:
        model = LessonSerializer.Meta.model
        fields = LessonSerializer.Meta.fields + ['content', 'tags']

class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password', 'email']
        extra_kwargs = {
            'password' : {
                'write_only': True
            }
        }

    def to_representation(self, instance):
        data = super().to_representation(instance)
        if instance.avatar:
            data['avatar'] = instance.avatar.url

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(user.password)
        user.save()


        return user