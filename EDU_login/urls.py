from django.urls import path

from EDU_login.views import log_out, login_page


urlpatterns = [
    path("login", login_page, name="login_page"),
    path("logout", log_out, name="logout_page")
]
