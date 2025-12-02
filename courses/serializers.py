from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer
from .models import Category, Course, Lesson, Tag, User, Comment


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
        fields = ['first_name', 'last_name', 'username', 'password', 'avatar']
        extra_kwargs = {
            'password' : {
                'write_only': True
            }
        }

    def to_representation(self, instance):
        data = super().to_representation(instance)
        if instance.avatar:
            data['avatar'] = instance.avatar.url if instance.avatar else ''
        return data

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(user.password)
        user.save()

        return user

    def update(self, instance, validated_data):
        keys = set(validated_data.keys())
        if keys - {'first_name', 'last_name', 'email'}:
            raise ValidationError({'error': 'Invalid fields'})

        return super().update(instance, validated_data)


class CommentSerializer(ModelSerializer):

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['user'] = UserSerializer(instance.user).data

        return data

    class Meta:
        model = Comment
        fields = ['id', 'content', 'created_date', 'user', 'lesson']
        extra_kwargs = {
            'lesson' : {
                'write_only': True
            }
        }