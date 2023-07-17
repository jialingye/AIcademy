from django.urls import path
from . import views
from .views import MyTokenObtainPairView

from rest_framework_simplejwt.views import(
    TokenRefreshView,
)
urlpatterns = [
    path('', views.getCourses, name="courses"),
    path('courses/', views.getCourses, name="courses"),
    path('courses/new/',views.createCourse, name="create_course"),
    path('courses/<int:pk>/update/', views.updateCourse, name="update_course"),
    path('courses/<int:pk>/delete/', views.deleteCourse, name="delete_course"),
    path('courses/<int:pk>/', views.getCourse, name="course"),
    path('courses/<int:pk>/lessons/new/', views.createLesson, name="create_lesson"),
    path('courses/<int:pk>/lessons/<int:lesson_pk>/', views.getLesson, name="lesson"),
    path('courses/<int:pk>/students/<int:student_pk>/', views.studentAsso, name = "student_asso"),
    path('lessons/<int:pk>/update/', views.updateLesson, name="update_lesson"),
    path('lessons/<int:pk>/delete/', views.deleteLesson, name="delete_lesson"),
    path('lessons/<int:pk>/assessments/', views.getAssessments, name="assessments"),
    path('lessons/<int:pk>/assessments/new/', views.createAssessment, name="create_assessments"),
    path('assessments/<int:pk>/update/', views.updateAssessment, name='update_assessment'),
    path('assessments/<int:pk>/delete/', views.deleteAssessment, name='delete_assessment'),
    path('assessments/<int:pk>/score/', views.createScore, name='create_score'),
    path('score/<int:pk>/update/', views.updateScore, name='update_score'),
    path('aiscore/', views.AiScore, name="ai_score"),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('collection/', views.GetCollections, name="get_collection"),
    path('collection/<int:pk>/', views.UserCollection, name="user_collection"),
    path('collection/new/', views.CollectionCreate, name="collection_create"),
    path('collection/<int:pk>/courses/<int:course_pk>/', views.CollectionAssoc, name="collection_assoc")
]