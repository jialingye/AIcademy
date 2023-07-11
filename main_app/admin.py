from django.contrib import admin

# Register your models here.

from .models import Course, CourseCollection, Lesson, Assessment,StudentInput,Score

admin.site.register(Course)
admin.site.register(Lesson)
admin.site.register(CourseCollection)
admin.site.register(Assessment)
admin.site.register(StudentInput)
admin.site.register(Score)

