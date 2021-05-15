from django.urls import path

from EDU_login.views import login_page


urlpatterns = [
    path("login", login_page, name="login_page")
]
