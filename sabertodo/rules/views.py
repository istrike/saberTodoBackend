from django.shortcuts import render

# Create your views here.

from rest_framework.viewsets import ModelViewSet

from .models import Rule
from .serializers import RuleSerializer


class RuleViewSet(ModelViewSet):
    queryset = Rule.objects.all().order_by("-id")
    serializer_class = RuleSerializer
    