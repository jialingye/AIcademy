from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    tag = models.CharField(max_length=100, default='Education')
    is_complete = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    instructor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="courses_created")
    students = models.ManyToManyField(User)

    def __str__(self):
        return self.title

class Lesson(models.Model):
    title = models.CharField(max_length=100)
    material = models.TextField()
    is_complete = models.BooleanField(default=False)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="lessons")

    class Meta:
        ordering = ['title']
        
    def __str__(self):
        return self.title

class Assessment(models.Model):
    question = models.TextField(max_length=1000)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name="assessments")
    

    def __str__(self):
        max_length= 100
        if len(self.question)> max_length:
            return self.question[:max_length-3]+"..."
        else:
            return self.question

class StudentInput(models.Model):
    input = models.TextField()
    assessment = models.ForeignKey(Assessment, on_delete=models.CASCADE, related_name="input")
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name="input")

    def __str__(self):
        max_length= 50
        if len(self.input)> max_length:
            return self.input[:max_length-3]+"..."
        else:
            return self.input

class Score(models.Model):
    assessment = models.ForeignKey(Assessment, on_delete=models.CASCADE, related_name="scores")
    score = models.IntegerField()
    input = models.TextField(default="")
    explanation = models.TextField()
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name="score")

    def __str__(self):
        max_length= 50
        if len(self.explanation)> max_length:
            return self.explanation[:max_length-3]+"..."
        else:
            return self.explanation


class CourseCollection(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length = 2000)
    course = models.ManyToManyField(Course)
    user= models.ManyToManyField(User)

    def __str__(self):
        return self.title