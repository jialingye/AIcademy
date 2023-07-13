from django.shortcuts import render
import openai
from django.conf import settings
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from django.contrib.auth.models import User
from .models import Course, Lesson, Assessment, Score
from .serializers import CourseSerializer, LessonSerializer, AssessmentSerializer, ScoreSerializer
# Create your views here.


@api_view(['GET'])
def getCourses(request):
    courses = Course.objects.all()
    serializer = CourseSerializer(courses, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getCourse(request, pk):
    course = Course.objects.get(id = pk)
    serializer = CourseSerializer(course, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def createCourse(request):
    user_id = request.data.get('instructor')
    try: 
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return Response({'error': 'User not found'}, status= status.HTTP_404_NOT_FOUND)
    title= request.data.get('title')
    description = request.data.get('description')
    tag = request.data.get('tag')

    course = Course.objects.create(
        title=title,
        description =description,
        tag=tag,
        instructor = user,
    )
    serializer = CourseSerializer(course, many=False)
    return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['PUT'])
def updateCourse(request, pk):
    try:
        course = Course.objects.get(id=pk)
    except Course.DoesNotExist:
        return Response({'error': 'Course not found'}, status=status.HTTP_404_NOT_FOUND)
    
    # if request.user != course.instructor:
    #     raise PermissionDenied('You do not have permission to update this course.')
    
    course.title = request.data.get('title', course.title)
    course.description = request.data.get('description', course.description)
    course.tag=request.data.get('tag', course.tag)
    course.save()
    serializer = CourseSerializer(course)

    return Response(serializer.data)

@api_view(['GET'])
def getLesson(request, pk, lesson_pk):
    lesson = Lesson.objects.get(course_id = pk, id = lesson_pk)
    serializer = LessonSerializer(lesson, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def createLesson(request, pk):
    try:
        course = Course.objects.get(id=pk)
    except Course.DoesNotExist:
        return Response({'error': 'Course not found'}, status=status.HTTP_404_NOT_FOUND)

    title= request.data.get('title')
    material = request.data.get('material')

    lesson = Lesson.objects.create(
        title=title,
        material=material,
        course=course
    )
    serializer = LessonSerializer(lesson, many=False)
    return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['PUT'])
def updateLesson(request, pk):
    try:
        lesson = Lesson.objects.get(id=pk)
    except Lesson.DoesNotExist:
        return Response({'error': 'Course not found'}, status=status.HTTP_404_NOT_FOUND)
    
    # if request.user != course.instructor:
    #     raise PermissionDenied('You do not have permission to update this course.')
    
    lesson.title = request.data.get('title', lesson.title)
    lesson.material = request.data.get('material', lesson.material)
    lesson.save()
    serializer = LessonSerializer(lesson)

    return Response(serializer.data)

@api_view(['GET'])
def getAssessments(request, pk):
    assessment = Assessment.objects.get(id = pk)
    serializer = LessonSerializer(assessment, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def createAssessment(request, pk):
    try:
        lesson = Lesson.objects.get(id=pk)
    except Lesson.DoesNotExist:
        return Response({'error': 'Course not found'}, status=status.HTTP_404_NOT_FOUND)

    question= request.data.get('question')

    assessment = Assessment.objects.create(
        question=question,
        lesson=lesson
    )
    serializer = AssessmentSerializer(assessment, many=False)
    return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['POST'])
def createScore(request, pk):
    user_id = request.data.get('student')
    try: 
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return Response({'error': 'User not found'}, status= status.HTTP_404_NOT_FOUND)
    
    assessment = Assessment.objects.get(id = pk)
    input_data = request.data.get('input','')
    score = request.data.get('score','')
    explanation = request.data.get('explanation')

    student_score = Score.objects.create(
        input=input_data,
        assessment=assessment,
        student=user,
        score=score,
        explanation=explanation
    )
    serializer = ScoreSerializer(student_score, many=False)
    return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['POST'])
def AiScore(request):
    question = request.data.get('question')
    answer = request.data.get('answer')

    try: 
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt = f'You are a Strict Teacher. This is the {question}, and this is the answer you provided:\n\n{answer}\n\nPlease carefully evaluate the answer and provide a score (0 to 10) and explanation based on the following criteria:\n\n1. Content Accuracy: Does the answer provide accurate information and address all aspects of the question?\n2. Overall Quality: Considering all the factors mentioned, assess the overall quality of the answer.\n\nPlease provide your assessment as follows:\n\nScore: [your score]\nExplanation: [your explanation]',
            max_tokens=1000,
            temperature=0.7,
            api_key=settings.OPENAI_API_KEY
        )

        answer = response.choices[0].text
        print(response)

        return Response(answer, status=status.HTTP_200_OK)
    except Exception as e:
        print('ChatGPT API request error:', str(e))
        return Response({'error':'An error occurred during the API request'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    