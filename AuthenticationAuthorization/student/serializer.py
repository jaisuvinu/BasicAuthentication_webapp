
from rest_framework import serializers
from student.models import Student, Faculty


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model= Student
        fields=['id','name','roll','city']

class FacultySerializer(serializers.ModelSerializer):
    class Meta:
        model= Faculty
        fields=['id','name','roll','city']

