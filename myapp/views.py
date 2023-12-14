from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework import generics, status
from rest_framework.response import Response
from django.db.models import F

from .models import Student, Subject
from .serializers import StudentsSerializer, SubjectSerializer, TableSerializer

@api_view(['GET'])
def hello_world(request, variant):
    response_data = {'message': f'Hello World {variant}'}
    return JsonResponse(response_data, status=200)

class StudentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentsSerializer

# Вигляд для деталей студентів, оновлення та видалення
class StudentDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentsSerializer

# Вигляд для списку предметів і створення нових предметів
class SubjectListCreateAPIView(generics.ListCreateAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

# Вигляд для деталей предметів, оновлення та видалення
class SubjectDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

class TableListAPIView(generics.ListCreateAPIView):
    queryset = Student.objects.order_by(F('rating').desc(nulls_last=True))  # Сортування за зменшенням рейтингу
    serializer_class = TableSerializer
