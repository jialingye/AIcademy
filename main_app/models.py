from django.db import models


# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    is_complete = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Lesson(models.Model):
    title = models.CharField(max_length=100)
    material = models.TextField()
    is_complete = models.BooleanField(default=False)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="lessons")

    def __str__(self):
        return self.title

class Assessment(models.Model):
    question = models.CharField(max_length=1000)
    answers = models.TextField()
    input = models.TextField()
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name="assessments")

    def __str__(self):
        return self.question


class CourseCollection(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length = 2000)
    course = models.ManyToManyField(Course)

    def __str__(self):
        return self.title