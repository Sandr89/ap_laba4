from rest_framework import serializers
from .models  import*

class StudentsSerializer(serializers.ModelSerializer):
    class Meta():
        model = Student
        fields = "__all__"

class SubjectSerializer(serializers.ModelSerializer):
    class Meta():
        model = Subject
        fields = "__all__"

class TableSerializer(serializers.ModelSerializer):
    class Meta():
        model = Student
        fields = '__all__'
