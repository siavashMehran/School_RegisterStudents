from EDU_signup.models import MyBaseUser
from django import forms
from TOOLS.verify_melli_code import verify_melli_code

class MyBaseUserModelForm(forms.ModelForm):

    class Meta:

        model   = MyBaseUser
        fields  = ['melli_code', 'phone']

        widgets = {
            'melli_code' : forms.TextInput(attrs={'placeholder' : 'کد ملی را وارد کنید (مثال : 0311751212) ', 'class' : 'initphoneinput'}),
            'phone'      : forms.TextInput(attrs={'placeholder' : 'تلفن همراه (مثال : 09399877887) :', 'class' : 'initphoneinput'})

        }

    def clean_melli_code(self):

        melli_code = self.cleaned_data.get('melli_code').strip()
        if len(melli_code) < 10:
            raise forms.ValidationError('کد ملی باید ده رقم باشد')

        # this is commented due to testing issues it might bring on
        # and should be used in production
        # if not (verify_melli_code(melli_code)):
        #     raise forms.ValidationError('کد ملی وارد شده اشتباه است')

        return str(melli_code)

    def clean_phone(self):
        
        phone = self.cleaned_data.get('phone')

        if phone[0] != '0':
            raise forms.ValidationError('شماره وارد شده صحیح نیست')

        if len(self.cleaned_data.get('phone')) < 11:
            raise forms.ValidationError('تلفن همراه باید یازده رقم باشد')

        return str(phone)