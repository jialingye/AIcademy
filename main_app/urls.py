from django.urls import path
from . import views

urlpatterns = [
    path('', views.getCourses, name="courses"),
    path('courses/', views.getCourses, name="courses"),
    path('courses/new/',views.createCourse, name="create_course"),
    path('courses/<int:pk>/update/', views.updateCourse, name="update_course"),
    path('courses/<int:pk>/', views.getCourse, name="course"),
    path('courses/<int:pk>/lessons/new/', views.createLesson, name="create_lesson"),
    path('courses/<int:pk>/lessons/<int:lesson_pk>/', views.getLesson, name="lesson"),
    path('lessons/<int:pk>/update/', views.updateLesson, name="updateLesson"),
    path('lessons/<int:pk>/assessments/', views.getAssessments, name="assessments"),
    path('lessons/<int:pk>/assessments/new', views.createAssessment, name="create_assessments"),
    path('assessments/<int:pk>/score/', views.createScore, name='create_score'),
    path('aiscore/', views.AiScore, name="ai_score")
]