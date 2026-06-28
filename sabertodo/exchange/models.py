from django.db import models
from student.models import Student
from rules.models import Rule

# Create your models here.
class Exchange(models.Model):
    Student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name="exchanges"
    )
    Rule = models.ForeignKey(
        Rule,
        on_delete=models.CASCADE,
        related_name="exchanges"
    )
    CostScore = models.IntegerField()
    GainEnergy = models.IntegerField()
    GainPetFood = models.IntegerField()
    CreateAt = models.DateTimeField(auto_now_add=True)
    UpdateAt = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = "exchange"

    def __str__(self):
        return f"{self.Student}-{self.CostScore}"