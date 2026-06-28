from rest_framework import serializers

from .models import Student


class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = "__all__"

    def validate_Score(self, value):
        if value < 0:
            raise serializers.ValidationError("积分不能小于0")
        return value

    def validate_Energy(self, value):
        if value < 0:
            raise serializers.ValidationError("能量不能小于0")
        return value

    def validate_PetFood(self, value):
        if value < 0:
            raise serializers.ValidationError("宠物粮不能小于0")
        return value