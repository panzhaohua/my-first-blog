# @Time    : 2021/3/22 18:10
# @Author  : MosesPan
# @Email   : 269258169@qq.com
# @File    : forms.py
# @Software: PyCharm

from django import forms

from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)