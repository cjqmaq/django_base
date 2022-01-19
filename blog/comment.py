from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from blog.models import Comment, Blog

import time


def add(request):
    comment = Comment()
    comment.content = request.POST['comment']
    comment.account = request.session['account']

    blog_id = request.POST['blog_id']
    blog = get_object_or_404(Blog,pk=blog_id)

    comment.blog = blog
    comment.pub_date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    comment.save()

    return HttpResponseRedirect(reverse('blog:details',kwargs={'blog_id':blog_id}))