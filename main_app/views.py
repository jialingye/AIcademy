from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Course, Lesson, Assessment
from .serializers import CourseSerializer, LessonSerializer
# Create your views here.

@api_view(['GET'])
def getRoutes(resquest):
    routes = [
        {
            'Endpoint': '/notes/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of notes'
        },
        {
            'Endpoint': '/notes/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single note object'
        },
        {
            'Endpoint': '/notes/create/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Creates new note with data sent in post request'
        },
        {
            'Endpoint': '/notes/id/update/',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Creates an existing note with data sent in post request'
        },
        {
            'Endpoint': '/notes/id/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes and exiting note'
        },
    ]
    return Response(routes)

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

@api_view(['PUT'])
def updateCourse(request, pk):
    data = request.data
    course = Course.objects.get(id=pk)
    serializer = CourseSerializer(instance=course, data=data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['GET'])
def getLesson(request, pk, lesson_pk):
    lesson = Lesson.objects.get(course_id = pk, id = lesson_pk)
    serializer = LessonSerializer(lesson, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def getAssessments(request, pk):
    assessment = Assessment.objects.get(id = pk)
    serializer = LessonSerializer(assessment, many=False)
    return Response(serializer.data)