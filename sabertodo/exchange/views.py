from django.shortcuts import render

# Create your views here.
from rest_framework import filters
from rest_framework.viewsets import ModelViewSet

from .models import Exchange
from .serializers import ExchangeSerializer


class ExchangeViewSet(ModelViewSet):

    queryset = Exchange.objects.select_related(
        "Student",
        "Rule"
    ).order_by("-id")

    serializer_class = ExchangeSerializer

    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

    search_fields = [
        "Student__Name",
        "Rule__Name",
    ]

    ordering_fields = [
        "id",
        "CostScore",
        "CreateAt",
    ]

    ordering = ["-id"]