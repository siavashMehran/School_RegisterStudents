from EDU_home.views import home
from django.urls import path

urlpatterns = [
    path('', home, name='index_page')
]
