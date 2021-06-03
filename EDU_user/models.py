from django.http.request import HttpRequest
from EDU_signup.models import MyBaseUser
from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.

class User_Auth_State(models.Model):

    GRADE_CHOICES = [('fourth' , 'چهارم'), ('fifth' , 'پنجم'), ('sixth' , 'ششم'), (None, 'انتخاب پایه')]

    user = models.OneToOneField(to=get_user_model(), on_delete=models.CASCADE)

    stu_first_name = models.CharField('نام', max_length=25, blank=False, )
    stu_last_name  = models.CharField('نام خانوادگی', max_length=25, blank=False)
    stu_father_name  = models.CharField('نام پدر', max_length=25, blank=False)

    stu_birthday    = models.CharField('تاریخ تولد', max_length=12, blank=True)

    stu_paye = models.CharField('پایه مورد نظر', max_length=15, choices=GRADE_CHOICES, blank=False)
    stu_last_moadel = models.CharField('معدل سال پیش', max_length=5, blank=True)


    def __str__(self):
        return f"{self.stu_first_name} {self.stu_last_name} / {self.stu_paye} / {self.user.username}"


class User_info_Deleter:

   

    
    def _delete_users_USER_AUTH_STATE(request):
        try:
            client_auth_table = User_Auth_State.objects.filter(user=request.user)
            if client_auth_table.exists():
                
                return client_auth_table.first().delete()
                
        except : pass

    
    def _delete_users_MyBaseUser(request:HttpRequest):
        try:
            client_MyBaseUser = MyBaseUser.objects.filter(melli_code=request.COOKIES.get('melli_code')).first()
            if client_MyBaseUser :
                return client_MyBaseUser.delete()
            else : pass
        except : pass

    def _delete_users_main_user(request):
        try:
            client_main_user_table = get_user_model().objects.get(username=request.user.username)
            if client_main_user_table:
                return client_main_user_table.delete()
            else : pass
        except : pass

    @classmethod
    def delete_user_all_related_tables(cls, request):
        cls._delete_users_MyBaseUser(request)
        cls._delete_users_USER_AUTH_STATE(request)