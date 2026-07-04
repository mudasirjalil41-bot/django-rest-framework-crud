
from django.core.serializers import serialize  # Unused, but kept intact
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Student
from .serializers import StudentSerializer


@api_view(["GET", "POST", "PUT", "PATCH", "DELETE"])
def student_api(request, pk=None):

    # --- GET Method ---
    if request.method == "GET":
        if pk is not None:
            try:
                stu = Student.objects.get(id=pk)
                serializer = StudentSerializer(stu)
                return Response(serializer.data)
            except Student.DoesNotExist:
                return Response(
                    {"error": "Student not found"},
                    status=status.HTTP_404_NOT_FOUND,
                )

        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        return Response(serializer.data)

    # --- POST Method ---
    elif request.method == "POST":
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # --- PUT Method ---
    elif request.method == "PUT":
        if pk is not None:
            try:
                stu = Student.objects.get(id=pk)
            except Student.DoesNotExist:
                return Response(
                    {"error": "Student not found"},
                    status=status.HTTP_404_NOT_FOUND,
                )

            serializer = StudentSerializer(stu, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )  # Fixed: Added invalid data fallback return

        return Response(
            {"error": "Method PUT requires an ID"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    # --- PATCH Method ---
    elif request.method == "PATCH":
        if pk is not None:
            try:
                stu = Student.objects.get(id=pk)
            except Student.DoesNotExist:
                return Response(
                    {"error": "Student not found"},
                    status=status.HTTP_404_NOT_FOUND,
                )

            serializer = StudentSerializer(stu, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )

        return Response(
            {"error": "Method PATCH requires an ID"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    # --- DELETE Method ---
    elif request.method == "DELETE":
        if pk is not None:
            try:
                stu = Student.objects.get(id=pk)
                stu.delete()
                return Response(
                    {"msg": "deleted successfully"},
                    status=status.HTTP_204_NO_CONTENT,
                )
            except Student.DoesNotExist:
                return Response(
                    {"error": "Student not found"},
                    status=status.HTTP_404_NOT_FOUND,
                )

        # Fixed: Cleared up the messy indentation spaces here
        return Response(
            {"error": "Method DELETE requires an ID"},
            status=status.HTTP_400_BAD_REQUEST,
        )