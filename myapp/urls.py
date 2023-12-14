from django.urls import path
from .views import hello_world, StudentListCreateAPIView, StudentDetailAPIView, SubjectListCreateAPIView, SubjectDetailAPIView, TableListAPIView

urlpatterns = [
    path('api/v1/hello-world-<int:variant>/', hello_world, name='hello_world'),
    path('students/', StudentListCreateAPIView.as_view(), name='student-list'),
    path('students/<int:pk>/', StudentDetailAPIView.as_view(), name='student-detail'),
    path('subjects/', SubjectListCreateAPIView.as_view(), name='subject-list'),
    path('subjects/<int:pk>/', SubjectDetailAPIView.as_view(), name='subject-detail'),
    path('table/', TableListAPIView.as_view(), name='table')
]