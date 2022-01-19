from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django_filters.rest_framework import DjangoFilterBackend

from .filter import BlogFilter
from .models import Blog, Account, Keywords, BlogKeywords, Comment
import time
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from rest_framework .generics import ListAPIView,RetrieveAPIView
from rest_framework.pagination import PageNumberPagination,LimitOffsetPagination
from rest_framework import viewsets
from  rest_framework import mixins
# Create your views here.

class BlogListViewSet(viewsets.GenericViewSet,mixins.ListModelMixin,mixins.RetrieveModelMixin,
                      mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin):
    '''

  通过判断action，返回不同的序列化
   '''
    serializer_class =  BlogSerializer
    queryset = Blog.objects.order_by('-pub_date')
    pagination_class = LimitOffsetPagination

    filter_backends = [DjangoFilterBackend]
    filterset_class = BlogFilter

    # def get_serializer_class(self):
    #     if self.action == 'list':
    #         return BlogSerializer
    #     elif self.action =='retrive':
    #         return BlogDetailSerializer
    #     else:
    #         return super().get_serializer_class()




class BlogListAPIView(ListAPIView):
    serializer_class = BlogSerializer
    queryset = Blog.objects.order_by('-pub_date')
    pagination_class = PageNumberPagination

class BlogDetaAPIView(RetrieveAPIView):
    serializer_class = BlogDetailSerializer

@api_view(http_method_names=['GET'])
def blog_list(request):
    blogs = Blog.objects.order_by('-pub_date')
    serializer = BlogSerializer(blogs,many=True)
    return Response(data=serializer.data,status=status.HTTP_200_OK)

@api_view(http_method_names=['GET'])
def Account_list(request):
    account_list = Account.objects.order_by('-user_name')
    serializer = AccountlistSerializer(account_list, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)

@api_view(http_method_names=['GET'])
def keyword_list(request):
    keywords = Keywords.objects.order_by('key_word')
    serializers = KeywordSerializer(keywords,many=True)
    return Response(data=serializers.data,status=status.HTTP_200_OK)
@api_view(http_method_names=['GET'])
def content(request,blog_id):
    blog_list = Blog.objects.get(pk=blog_id)
    serializers = ContentSerializer(blog_list,many=False)
    return Response(data=serializers.data,status=status.HTTP_200_OK)

@api_view(http_method_names=['GET'])
def Comment(requets,blog_id):
    blog = Blog.objects.get(pk=blog_id)
    comments = blog.comment_set.all()
    serializers = CommentSerializer(comments, many=True)
    return Response(data=serializers.data, status=status.HTTP_200_OK)





def index(reqeust):
    blog_list = Blog.objects.order_by('-pub_date')
    account_list = Account.objects.order_by('-user_name')


    # context = {
    #     'blog_list':blog_list,
    #     'account_list':account_list,
    # }



    # if 'account' in reqeust.session:
    #     context['account'] = reqeust.session['account']

    return render(reqeust, 'blog/index.html', locals())

def details(request,blog_id):
    '''
    把数据库数据取出来，传给前段，展示出来
    :param request:
    :param blog_id:
    :return:
    '''
    # 方法1
    # try:
    #     blog = Blog.objects.get(pk=blog_id)
    #
    # except Blog.DoesNotExist:
    #   raise Http404('blog not found')
    # 方法2
    blog = get_object_or_404(Blog,pk=blog_id)
    return render(request,'blog/details.html',{'blog':blog})


def add(request):
    '''
    点击添加跳转
    :param request:
    :return:
    '''
    # return HttpResponse('add')
    if 'account' in request.session:
       return render(request,'blog/add.html')
    else:
       return HttpResponseRedirect(reverse('blog:login'))

def add_save(request):
    '''
    添加博客内容
    :param request:
    :return:
    '''
    if 'account' in request.session:
        blog = Blog()
        key_words = request.POST['key_words']
        blog.title = request.POST['title']
        blog.content = request.POST['content']
        blog.key_words = key_words
        blog.account = request.session['account']

        blog.pub_date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        blog.save()
        # 保存关键字
        keys = key_words.split(',')
        for key in keys:
            kw = Keywords()
            kw.key_word = key
            kw.save()

            blog_key = BlogKeywords()
            blog_key.blog = blog
            blog_key.key_word = kw
            blog_key.save()

        return render(request, 'blog/details.html', {'blog': blog})

    else:
        return render(request, 'blog/add.html')

def edit(request,blog_id):
    '''
    点击修改跳转
    :param request:
    :param blog_id:
    :return:
    '''
    if 'account' in request.session:
        blog = get_object_or_404(Blog, pk=blog_id)
        return render(request, 'blog/edit.html', {'blog': blog})

    else:
        return render(request, 'blog/add.html')



def edit_save(request):
    '''
    修改博客内容
    :param request:
    :return:
    '''
    if 'account' in request.session:
        blog = get_object_or_404(Blog, pk=request.POST['blog_id'])
        blog.title = request.POST['title']
        blog.content = request.POST['content']
        blog.save()
        return render(request, 'blog/details.html', {'blog': blog})

    else:
        return render(request, 'blog/add.html')


def blog_by_account(request,account_id):
    blog_list = Blog.objects.filter(account=Account.objects.get(pk=account_id))
    return render(request,'blog/blog_list.html',{'blog_list':blog_list})


def approval(request,blog_id,comment_id,opra):
    comment = get_object_or_404(Comment,pk = comment_id)
    if opra ==1:
       comment.approval += 1
    else:
        comment.oppose += 1
    comment.save()
    return HttpResponseRedirect(reverse('blog:details',kwargs={'blog_id':blog_id}))

# def oppose(request,blog_id,comment_id):
#     comment = get_object_or_404(Comment, pk=comment_id)
#     comment.oppose = comment.oppose+1
#     comment.save()
#     return HttpResponseRedirect(reverse('blog:details', kwargs={'blog_id': blog_id}))









