from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import  io



@csrf_exempt
def student_create(request):
    if request.method == "POST":
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        serializer = StudentSerializer(data = python_data)
        if serializer.is_valid():
            serializer.save()
            response = {"msg":"data inserted"}
            json_data = JSONRenderer().render(response)
            return HttpResponse(json_data, content_type = "application/json")
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type="application/json")
    if request.method == "PUT":
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        stu = Student.objects.get(id = id)
        serializer = StudentSerializer(stu,data = python_data, partial = True)
        if serializer.is_valid():
            serializer.save()
            response = {"mssg":"updated successfully"}
            json_data = JSONRenderer().render(response)
            return HttpResponse(json_data, content_type="application/json")
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type="application/json")
    if request.method == 'GET':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get("id",None)
        if id is not None:
           stu = Student.objects.get(id = id)
           serializer = StudentSerializer(stu)

        else:
            stu = Student.objects.all()
            serializer = StudentSerializer(stu, many = True)

        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data, content_type="application/json")


    if request.method == "DELETE":
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get("id")
        stu = Student.objects.get(id = id)
        stu.delete()
        response = {"mssg":"deleted successfully"}
        json_data = JSONRenderer().render(response)
        return HttpResponse(json_data, content_type="application/json")




