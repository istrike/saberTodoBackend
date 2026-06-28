from django.shortcuts import render

# Create your views here.
from rest_framework import filters
from rest_framework.viewsets import ModelViewSet

from .models import Student
from .serializers import StudentSerializer


class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all().order_by("-id")
    serializer_class = StudentSerializer

    filter_backends = [filters.SearchFilter, filters.OrderingFilter]

    search_fields = [
        "Name",
        "Phone",
    ]

    ordering_fields = [
        "id",
        "Score",
        "Energy",
        "CreateAt",
    ]

    ordering = ["-id"]