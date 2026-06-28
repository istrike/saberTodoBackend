from django.db import models
from task.models import Task
from student.models import Student


class StatusType(models.IntegerChoices):
    NOT_START = 0, "未开始"
    IN_PROGRESS = 1, "进行中"
    FINISHED = 2, "已完成"


class StudentTask(models.Model):

    Student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name="tasks"
    )

    Task = models.ForeignKey(
        Task,
        on_delete=models.CASCADE,
        related_name="student_tasks"
    )

    Status = models.IntegerField(
        choices=StatusType.choices,
        default=StatusType.NOT_START
    )
    FinishedAt = models.DateTimeField(null=True, blank=True)
    CreateAt = models.DateTimeField(auto_now_add=True)
    UpdateAt = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "student_task"

    def __str__(self):
        return f"{self.Student.Name}-{self.Task.Name}"