from rest_framework import serializers

from .models import Exchange


class ExchangeSerializer(serializers.ModelSerializer):

    StudentName = serializers.CharField(
        source="Student.Name",
        read_only=True
    )

    RuleName = serializers.CharField(
        source="Rule.Name",
        read_only=True
    )

    class Meta:
        model = Exchange
        fields = "__all__"