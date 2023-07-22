from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Course, Lesson, Assessment, Score, CourseCollection
from django.contrib.auth.models import User

class ScoreSerializer(ModelSerializer):
    class Meta:
        model = Score
        fields = '__all__'

class AssessmentSerializer(ModelSerializer):
    scores = ScoreSerializer(many=True, read_only=True)
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

class CollectionSerializer(ModelSerializer):
    course = CourseSerializer(many=True, read_only=True)
    class Meta:
        model = CourseCollection
        fields = '__all__'
    
class UserRegistrationSerializer(ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validate_data):
        password = validate_data.pop('password',None)
        instance= self.Meta.model(**validate_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance