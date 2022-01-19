from django.urls import path, include
from . import views, comment
from . import account
from rest_framework import routers

# 生成API的交互跟视图
api_router = routers.DefaultRouter()
api_router.register('blog',views.BlogListViewSet,basename='blogs')

app_name = 'blog'
urlpatterns = [
    path('api/',include(api_router.urls)),
    path('',views.index,name='index'),
    path('list/',views.blog_list,name='list'),
    path('list2/',views.BlogListAPIView.as_view(),name='list2'),
    path('account/',views.Account_list,name='account'),
    path('keyword/',views.keyword_list,name='keyword'),
    path('comment/<int:blog_id>',views.Comment,name='Comment'),
    path('content/<int:blog_id>',views.content,name='content'),
    path('<int:blog_id>/details/',views.details,name='details'),
    path('add/',views.add,name='add'),
    path('<int:blog_id>/edit/',views.edit,name='edit'),
    path('add_save/',views.add_save,name='add_save'),
    path('edit_save/',views.edit_save,name='edit_save'),
    path('login/',account.login,name='login'),
    path('login_check/',account.login_check,name='login_check'),
    path('logout/',account.logout,name='logout'),
    path('regist/',account.regist,name='regist'),
    path('reg/',account.regist_page,name='reg'),
    path('<int:account_id>/',views.blog_by_account,name='account'),
    path('comment_add/',comment.add,name='comment_add'),
    path('<int:blog_id>/approval/<int:comment_id>/<int:opra>',views.approval,name='approval'),
    # path('<int:blog_id>/oppose/<int:comment_id>', views.oppose, name='oppose')

]