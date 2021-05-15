from django.urls import path
from EDU_signup.views import home, pre_validate

urlpatterns = [
    path('', home),
    path('signup', pre_validate, name='pre_validate')
]
