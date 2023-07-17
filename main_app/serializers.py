from rest_framework.serializers import ModelSerializer
from .models import Course, Lesson, Assessment, Score, CourseCollection

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
    class Meta:
        model = CourseCollection
        fields = '__all__'