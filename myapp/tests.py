from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Student, Subject
from .serializers import StudentsSerializer, SubjectSerializer, TableSerializer

class StudentAPITests(APITestCase):
    def setUp(self):
        self.student = Student.objects.create(name='John', rating=80)

    def test_student_list_create(self):
        url = reverse('student-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_student_detail(self):
        url = reverse('student-detail', kwargs={'pk': self.student.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'John')


    def test_student_delete(self):
        url = reverse('student-detail', kwargs={'pk': self.student.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        with self.assertRaises(Student.DoesNotExist):
            Student.objects.get(pk=self.student.pk)


class SubjectAPITests(APITestCase):
    def setUp(self):
        self.subject = Subject.objects.create(name='Math')

    def test_invalid_subject_create(self):
        url = reverse('subject-list')
        data = {'invalid_field': 'Invalid Subject'}  # Missing 'name' field
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_subject_not_found(self):
        url = reverse('subject-detail', kwargs={'pk': 999})  # Replace with a non-existent ID
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
    def test_subject_list_create(self):
        url = reverse('subject-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_subject_detail(self):
        url = reverse('subject-detail', kwargs={'pk': self.subject.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Math')

    def test_subject_create(self):
        url = reverse('subject-list')
        data = {'name': 'Science'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_subject_update(self):
        url = reverse('subject-detail', kwargs={'pk': self.subject.pk})
        data = {'name': 'Math Updated'}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        updated_subject = Subject.objects.get(pk=self.subject.pk)
        self.assertEqual(updated_subject.name, 'Math Updated')

    def test_subject_delete(self):
        url = reverse('subject-detail', kwargs={'pk': self.subject.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        with self.assertRaises(Subject.DoesNotExist):
            Subject.objects.get(pk=self.subject.pk)