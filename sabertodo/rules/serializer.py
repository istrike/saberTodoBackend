from rest_framework import serializers
from .models import Rule

class RuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rule
        fields = '__all__'

    def create(self,validated_data):
        rule = Rule.objects.create(**validated_data)
        return rule 
    def validate_NeedScore(self, value):
        if value < 0:
            raise serializers.ValidationError("NeedScore不能小于0")
        return value

    def validate(self, attrs):
        if attrs["RewardEnergy"] < 0:
            raise serializers.ValidationError("RewardEnergy不能小于0")
        return attrs