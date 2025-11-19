from django.db import models
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField
from cloudinary.models import CloudinaryField
from django.db.models import CharField


class User(AbstractUser):
    avatar = CloudinaryField(null=True)

class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Course(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True)
    image = CloudinaryField(null=True) #models.ImageField(upload_to='courses/%Y/%m/', null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Lesson(BaseModel):
    name = models.CharField(max_length=255)
    content = RichTextField()
    image = CloudinaryField(null=True) #models.ImageField(upload_to='lessons/%Y/%m', null=True)
    course = models.ForeignKey(Course, on_delete=models.RESTRICT)
    tags = models.ManyToManyField('Tag')

    def __str__(self):
        return self.name

    class Meta:
        unique_together = ('name', 'course')


class Tag(BaseModel):
    name = CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
