from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Student(models.Model):
    Name = models.CharField(max_length=40)
    Phone = PhoneNumberField()
    Score = models.IntegerField(default=0)
    Energy = models.IntegerField(default=0)
    PetFood = models.IntegerField(default=0)
    CreateAt = models.DateTimeField(auto_now_add=True)
    UpdateAt = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "student"

    def __str__(self):
        return f"{self.Name}"