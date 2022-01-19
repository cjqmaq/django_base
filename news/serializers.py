from rest_framework import serializers
from .models import *

class Newsserializer(serializers.ModelSerializer):
    class Meta:
        model = news
        fields = ['id','title','author','url']