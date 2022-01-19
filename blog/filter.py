from django_filters import rest_framework

from blog.models import Blog

class BlogFilter(rest_framework.FilterSet):

    class Meta:
        model = Blog
        fields = ['account','title']