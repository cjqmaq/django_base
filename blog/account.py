from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import Blog,Account
import time


def login(request):
    '''
    登录跳转到login_cjeck
    :param request:
    :return:
    '''

    return render(request,'blog/login.html')


def login_check(request):
   '''
  登录后台需要处理的过程
  :param request:
  :return:
   '''
   user_name = request.POST['user_name']
   pass_word = request.POST['pass_word']
   print(user_name,pass_word)
   account = Account.objects.filter(user_name=user_name)
   msg=''
   if (len(account) == 0):
       msg='用户名不存在'
       # return  render(request,'blog/login.html',{'msg':msg})
   else:
      if pass_word == account[0].pass_word:

         request.session['account'] = account[0]

         return HttpResponseRedirect(reverse('blog:index'))
      else:
          msg='密码错误'

   return render(request, 'blog/login.html', {'msg': msg})

def logout(request):
    request.session.flush()
    return HttpResponseRedirect(reverse('blog:index'))

def regist(request):

    account = Account()
    account.user_name = request.POST['user_name']
    account.pass_word = request.POST['pass_word']
    account.last_login_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
    account.save()
    return  HttpResponseRedirect(reverse('blog:login'))

def regist_page(request):
    return  render(request,'blog/regist.html')