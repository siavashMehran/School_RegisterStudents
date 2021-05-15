from EDU_signup.views import home, pre_validate
from django.urls import path

urlpatterns = [
    path('', home),
    path('signup', pre_validate, name='pre_validate')
]
