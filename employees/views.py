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

    def post(self, request):
        serializer = DepartmentsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def decode_csv(file_string, field_name):
    rows = []
    for row in file_string.split('\r\r\n'):
        fields = row.split(',')
        diction = {}
        for i in range(len(field_name)):
            diction[field_name[i]] = fields[i]
        rows.append(diction)
    return rows


class UploadAPIView(views.APIView):
    def is_all_rows_valid(self, serializer, rows):
        all_valid = True
        for dictionary in rows:
            serializer = serializer(data=dictionary)
            if serializer.is_valid():
                all_valid = True
            else:
                all_valid = False
                break
        return all_valid

    def insert(self, serializer, rows):
        for dictionary in rows:
            serializer = serializer(data=dictionary)
            if serializer.is_valid():
                serializer.save()

    def post(self, request):
        file_uploaded = request.FILES.get('file_uploaded')
        fields_name = ['id', 'department']
        rows_in_dict = decode_csv(file_uploaded.read().decode(), fields_name)
        are_valid = self.is_all_rows_valid(DepartmentsSerializer, rows_in_dict)

        if are_valid:
            self.insert(DepartmentsSerializer, rows_in_dict)
            return Response("OK", status=status.HTTP_201_CREATED)
        else:
            return Response("error", status=status.HTTP_400_BAD_REQUEST)
