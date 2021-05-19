from EDU_user.models import User_Auth_State
from django import forms



class User_Auth_State_Model_Form(forms.ModelForm):

    class Meta:
    
        model   = User_Auth_State
        fields  = ['stu_first_name', 'stu_last_name', 'stu_father_name', 'stu_birthday', 'stu_paye', 'stu_last_moadel', 'user']

        widgets = {
            'stu_first_name'  : forms.TextInput(attrs={'placeholder' : 'نام دانش آموز :', 'class' : 'initphoneinput'}),
            'stu_last_name'   : forms.TextInput(attrs={'placeholder' : 'نام خانوادگی :', 'class' : 'initphoneinput'}),
            'stu_father_name' : forms.TextInput(attrs={'placeholder' : 'نام پدر :', 'class' : 'initphoneinput'}),
            'stu_birthday'    : forms.TextInput(attrs={'placeholder' : 'تاریخ تولد ( مثال  1382-12-30 ):', 'class' : 'initphoneinput'}),
            'stu_last_moadel' : forms.TextInput(attrs={'placeholder' : 'آخرین معدل دانش آموز به صورت ( 19.34 ):', 'class' : 'initphoneinput'}),
            'user'            : forms.HiddenInput({'required': 'false'}),
            'stu_paye'        : forms.Select(attrs={'class' : 'initphoneinput'}),
        }