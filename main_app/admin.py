from django.contrib import admin

# Register your models here.

from .models import Course, CourseCollection, Lesson, Assessment,Score

admin.site.register(Course)
admin.site.register(Lesson)
admin.site.register(CourseCollection)
admin.site.register(Assessment)
admin.site.register(Score)

