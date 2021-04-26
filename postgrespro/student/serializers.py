from rest_framework import serializers
from .models import Student,District


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('__all__')

class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = ('__all__')