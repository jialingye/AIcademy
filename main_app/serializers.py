from rest_framework.serializers import ModelSerializer
from .models import Course, Lesson, Assessment

class AssessmentSerializer(ModelSerializer):
    class Meta:
        model = Assessment
        fields = '__all__'
        
class LessonSerializer(ModelSerializer):
    assessments = AssessmentSerializer(many=True, read_only=True)
    class Meta:
        model = Lesson
        fields = '__all__'

class CourseSerializer(ModelSerializer):
    lessons = LessonSerializer(many=True, read_only=True)
    class Meta:
        model = Course
        fields = ['id','title', 'description', 'tag', 'is_complete', 'updated', 'created', 'instructor', 'students', 'lessons']

