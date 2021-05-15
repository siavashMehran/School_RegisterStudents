from EDU_signup.models import MyBaseUser
from django import forms


class MyBaseUserModelForm(forms.ModelForm):

    class Meta:

        model   = MyBaseUser
        fields  = ['melli_code', 'phone']

        widgets = {
            'melli_code' : forms.TextInput(attrs={'placeholder' : 'کد ملی را وارد کنید (مثال : 0311751212) ', 'class' : 'initphoneinput'}),
            'phone'      : forms.TextInput(attrs={'placeholder' : 'تلفن همراه (مثال : 09399877887) :', 'class' : 'initphoneinput'})

        }

    def clean_melli_code(self):
        melli_code = self.cleaned_data.get('melli_code')
        if len(melli_code) < 10:
            raise forms.ValidationError('کد ملی باید ده رقم باشد')
        return str(melli_code)

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if len(self.cleaned_data.get('phone')) < 11:
            raise forms.ValidationError('تلفن همراه باید یازده رقم باشد')
        return str(phone)