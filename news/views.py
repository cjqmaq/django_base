from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import mixins
from django_filters.rest_framework import DjangoFilterBackend
from .filter import NewsFilter
from rest_framework.pagination import *
from .serializers import *
from .models import *

# Create your views here.

class NewsListViewSet(viewsets.GenericViewSet,mixins.ListModelMixin,mixins.DestroyModelMixin,mixins.UpdateModelMixin,mixins.CreateModelMixin,mixins.RetrieveModelMixin):
    serializer_class =  Newsserializer
    queryset = news.objects.order_by('-pub_time')
    pagination_class = PageNumberPagination

    filter_backends = [DjangoFilterBackend]
    filterset_class = NewsFilter