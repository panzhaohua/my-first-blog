# @Time    : 2021/3/19 16:54
# @Author  : MosesPan
# @Email   : 269258169@qq.com
# @File    : urls.py
# @Software: PyCharm

from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]