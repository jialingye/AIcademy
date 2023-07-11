from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes, name="routes"),
    path('courses/', views.getCourses, name="courses"),
    path('courses/<int:pk>/update/', views.updateCourse, name="update_course"),
    path('courses/<int:pk>/', views.getCourse, name="course"),
    path('courses/<int:pk>/lessons/<int:lesson_pk>/', views.getLesson, name="lesson"),
    path('lessons/<int:pk>/assessments/', views.getAssessments, name="assessments"),
]