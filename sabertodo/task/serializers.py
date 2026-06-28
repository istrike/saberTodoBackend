from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = "__all__"

    def validate_NeedScore(self, value):
        if value < 0:
            raise serializers.ValidationError("NeedScore不能小于0")
        return value

    def validate(self, attrs):
        if attrs["RewardEnergy"] < 0:
            raise serializers.ValidationError("RewardEnergy不能小于0")

        if attrs["RewardPetFood"] < 0:
            raise serializers.ValidationError("RewardPetFood不能小于0")

        return attrs