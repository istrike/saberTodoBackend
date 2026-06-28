from django.db import models

# Create your models here.
class Rule(models.Model):
    Name = models.CharField(max_length=100)
    NeedScore = models.IntegerField()
    RewardEnergy = models.IntegerField()
    RewardPetFood = models.IntegerField()
    CreateAt = models.DateTimeField(auto_now_add=True)
    UpdateAt = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = "rule"

    def __str__(self):
        return self.name