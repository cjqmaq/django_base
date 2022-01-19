from rest_framework import serializers
from .models import *

class AccountlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'
class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'

class BlogSerializer(serializers.ModelSerializer):
    '''
    用于展示博客列表的序列化引擎
    '''
    # account = AccountlistSerializer()

    class Meta:
        model = Blog
        fields = '__all__'
class BlogDetailSerializer(serializers.ModelSerializer):
    '''
    用于展示博客列表的序列化引擎
    '''
    account = AccountlistSerializer()

    class Meta:
        model = Blog
        fields = '__all__'

class KeywordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Keywords
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    account = AccountlistSerializer()
    class Meta:
        model = Comment
        fields = '__all__'
