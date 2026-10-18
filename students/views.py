from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import StudentModel
from .serializers import StudentSerializer


class StudentListCreateAPIView(APIView):

    # GET: সব student দেখাবে
    def get(self, request):
        students = StudentModel.objects.all()
        serializer = StudentSerializer(students, many=True)

        return Response(
            {
                "success": True,
                "message": "Data getting seccessfully.",
                "data": serializer.data,
            },
            status=status.HTTP_200_OK,
        )

    # POST: নতুন student তৈরি করবে
    def post(self, request):
        serializer = StudentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(
                {
                    "success": True,
                    "message": "Data create successfully.",
                    "data": serializer.data,
                },
                status=status.HTTP_201_CREATED,
            )

        else:
            return Response(
                {
                    "success": False,
                    "message": "Invalid data.",
                    "errors": serializer.data,
                },
                status=status.HTTP_400_BAD_REQUEST,
            )


class StudentDetailAPIView(APIView):

    # নির্দিষ্ট student খুঁজে বের করবে
    def get_student(self, pk):
        return get_object_or_404(StudentModel, pk=pk)

    # GET: একজন student-এর তথ্য দেখাব
    def get(self, request, pk):
        student = self.get_student(pk)
        serializer = StudentSerializer(student)

        return Response(
            {
                "success": True,
                "message": "Data getting seccessfully.",
                "data": serializer.data,
            },
            status=status.HTTP_200_OK,
        )

    # PUT: সব প্রয়োজনীয় field আপডেট করব
    def put(self, request, pk):
        student = self.get_student(pk)
        serializer = StudentSerializer(student, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(
                {
                    "success": True,
                    "message": "Data updated successfully.",
                    "data": serializer.data,
                },
                status=status.HTTP_200_OK,
            )

        else:
            return Response(
                {
                    "success": False,
                    "message": "Invalid data.",
                    "errors": serializer.data,
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

    # PUT: সব প্রয়োজনীয় field আপডেট করব
    def put(self, request, pk):
        student = self.get_student(pk)
        serializer = StudentSerializer(student, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(
                {
                    "success": True,
                    "message": "Data updated successfully.",
                    "data": serializer.data,
                },
                status=status.HTTP_200_OK,
            )

        else:
            return Response(
                {
                    "success": False,
                    "message": "Invalid data.",
                    "errors": serializer.data,
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

    # PATCH: নির্দিষ্ট field আপডেট করব
    def patch(self, request, pk):
        student = self.get_student(pk)
        serializer = StudentSerializer(student, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()

            return Response(
                {
                    "success": True,
                    "message": "Data updated successfully.",
                    "data": serializer.data,
                },
                status=status.HTTP_200_OK,
            )

        else:
            return Response(
                {
                    "success": False,
                    "message": "Invalid data.",
                    "errors": serializer.data,
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

    # DELETE: student মুছে ফেলবে
    def delete(self, request, pk):
        student = self.get_student(pk)
        student.delete()

        return Response(
            {
                "success": True,
                "message": "Data deleted successfully.",
            },
            status=status.HTTP_200_OK,
        )
