# student_task/serializers.py

from rest_framework import serializers
from .models import StudentTask,Student

class StudentTaskSimpleSerializer(serializers.ModelSerializer):
    task_name = serializers.CharField(source="Task.Name", read_only=True)

    class Meta:
        model = StudentTask
        fields = [
            "id",
            "Status",
            "FinishedAt",
            "task_name",
        ]

from student_task.serializers import StudentTaskSimpleSerializer

class StudentSerializer(serializers.ModelSerializer):
    tasks = StudentTaskSimpleSerializer(many=True, read_only=True)

    class Meta:
        model = Student
        fields = "__all__"