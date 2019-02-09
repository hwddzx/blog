from django import forms

from blog.models import MessageBoard, User


class MessageBoardForm(forms.ModelForm):
    """留言板表单验证"""

    class Meta:
        model = MessageBoard
        # 需要验证的字段
        fields = ['content', ]
        error_messages = {
            'content': {
                'required': '留言内容不能为空!'
            }
        }


class UserForm(forms.ModelForm):
    """用户注册验证"""
    # 单独添加字段
    password = forms.CharField(max_length=16,
                               min_length=6,
                               error_messages={
                                   'required': '密码不能为空',
                                   'max_length': '密码长度不能大于16个字符',
                                   'min_length': '密码长度不能大于16个字符'
                               })

    repassword = forms.CharField(error_messages={'required': '确认密码不能为空'})

    class Meta:
        model = User
        fields = ['phone', ]
        error_messages = {
            'phone': {
                'required': '手机号不能为空'
            }
        }
