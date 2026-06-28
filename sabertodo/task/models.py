from django.db import models

class RepeatType(models.IntegerChoices):
    ONCE = 0, "一次"
    DAILY = 1, "每天"
    WEEKLY = 2, "每周"
    MONTHLY = 3, "每月"
    

# Create your models here.
class Task(models.Model):
    Name = models.CharField(max_length=100)
    Description = models.CharField(max_length=100)
    TaskType = models.IntegerField()
    RepeatType = models.IntegerChoices(
        choices=RepeatType.choices,
        default=RepeatType.ONCE
    )
    Enable = models.BooleanField()
    NeedScore = models.IntegerField()
    RewardEnergy = models.IntegerField()
    RewardPetFood = models.IntegerField()
    CreateAt = models.DateTimeField(auto_now_add=True)
    UpdateAt = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = "task"

    def __str__(self):
        return self.Name