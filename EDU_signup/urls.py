from django.urls import path
from EDU_signup.views import pre_validate, signup

urlpatterns = [
    path('signup', signup, name='signup_page'),
    path('validate', pre_validate, name='pre_validate_page')
]
