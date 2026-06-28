from django.db import models

# Create your models here.
class Pet(models.Model):
    Name = models.CharField(max_length=100)
    Level = models.IntegerField()
    Energy = models.IntegerField()
    CreateAt = models.DateTimeField(auto_now_add=True)
    UpdateAt = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = "Pet"

    def __str__(self):
        return self.Name