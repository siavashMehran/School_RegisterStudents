from django.urls import path
from EDU_signup.views import signup, phone_number_validate

urlpatterns = [
    path('signup', signup, name='signup_page'),
    path('signup/validate', phone_number_validate, name='phone_number_validate_page')
]
