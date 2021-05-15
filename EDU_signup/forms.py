from EDU_signup.models import MyBaseUser
from django import forms


class MyBaseUserModelForm(forms.ModelForm):

    class Meta:

        model   = MyBaseUser
        fields  = ['melli_code', 'phone']

        widgets = {
            'melli_code' : forms.NumberInput(attrs={'placeholder' : 'کد ملی را وارد کنید (مثال : 0311751212) ', 'class' : 'initphoneinput'}),
            'phone'      : forms.NumberInput(attrs={'placeholder' : 'تلفن همراه (مثال : 09399877887) :', 'class' : 'initphoneinput'})

        }
