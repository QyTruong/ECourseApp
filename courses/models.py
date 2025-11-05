from django.db import models
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField


class User(AbstractUser):
    pass

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
    image = models.ImageField(upload_to='courses/%Y/%m/', null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Lesson(BaseModel):
    name = models.CharField(max_length=255)
    content = RichTextField()
    image = models.ImageField(upload_to='lessons/%Y/%m', null=True)
    course = models.ForeignKey(Course, on_delete=models.RESTRICT)

    def __str__(self):
        return self.name


