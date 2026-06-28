from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet

from .models import Task
from .serializers import TaskSerializer


class TaskViewSet(ModelViewSet):
    serializer_class = TaskSerializer

    def get_queryset(self):
        queryset = Task.objects.all().order_by("-id")

        enable = self.request.query_params.get("enable")
        task_type = self.request.query_params.get("task_type")
        repeat_type = self.request.query_params.get("repeat_type")

        if enable is not None:
            queryset = queryset.filter(Enable=enable.lower() == "true")

        if task_type:
            queryset = queryset.filter(TaskType=task_type)

        if repeat_type:
            queryset = queryset.filter(RepeatType=repeat_type)

        return queryset