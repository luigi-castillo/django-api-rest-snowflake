from rest_framework import serializers
from .models import Departments


class DepartmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departments
        fields = ['id','department']

class UploadSerializer(serializers.Serializer):
    file_uploaded = serializers.FileField()
    class Meta:
        fields = ['file_uploaded']