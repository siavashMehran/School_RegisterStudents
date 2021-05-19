from EDU_user.views import personal_info
from django.urls import path
urlpatterns = [
    path('signup/validate/personal-info', personal_info, name='personal_info_page')
]
