from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse

def student_detail(request,pk):
    student = Student.objects.get(id = pk)
    serializer = StudentSerializer(student)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type = "application/json")

