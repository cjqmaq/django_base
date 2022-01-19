from django.urls import path, include
from . import views

from rest_framework import routers

api_router = routers.DefaultRouter()
api_router.register('new',views.NewsListViewSet,basename='news')

app_name = 'news'
urlpatterns = [
    path('api/',include(api_router.urls)),
]