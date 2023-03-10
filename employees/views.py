from django.shortcuts import render
# from rest_framework import viewsets
# from .models import Departments
# from .serializers import DepartmentsSerializer
#
#
# # Create your views here.
# class DepartmentsViewSet(viewsets.ModelViewSet):
#     serializer_class = DepartmentsSerializer
#     queryset = Departments.objects.all()
from rest_framework import views, status
from rest_framework.response import Response

from .models import Departments
from .serializers import DepartmentsSerializer, UploadSerializer


# Create your views here.
class DepartmentsAPIView(views.APIView):
    def get(self, request):
        depts = Departments.objects.all()
        serializer = DepartmentsSerializer(depts, many=True)
        return Response(serializer.data)


class UploadAPIView(views.APIView):
    def post(self, request):
        file_uploaded = request.FILES.get('file_uploaded')
        file_name = file_uploaded.name
        file_data = []
        for row in file_uploaded.read().decode().split('\r\r\n'):
            file_data.append(row)
        response = file_data
        return Response(response)
        # serializer = DepartmentsSerializer(data=request.data)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
