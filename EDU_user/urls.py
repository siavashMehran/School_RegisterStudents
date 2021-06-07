from EDU_user.views import personal_info, upload_page
from django.urls import path
urlpatterns = [
    path('signup/validate/personal-info', personal_info, name='personal_info_page'),
    path('signup/validate/personal-info/upload', upload_page, name='upload_page')
]
