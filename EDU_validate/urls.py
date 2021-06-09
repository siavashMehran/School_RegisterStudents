
from EDU_validate.views import verify_page
from django.urls.conf import path


urlpatterns = [
    path('signup/validate/personal-info/upload/verify', verify_page, name='verify_page')
]
