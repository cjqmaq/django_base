from  django_filters import rest_framework

from news.models import news

class NewsFilter(rest_framework.FilterSet):

    class Meta:
        model = news
        fields = ['text','title']