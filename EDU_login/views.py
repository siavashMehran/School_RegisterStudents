from django.http.request import HttpRequest
from EDU_user.models import User_info_Deleter
from django.http.response import Http404, HttpResponse
from django.shortcuts import redirect, render

# authenticate related import
from django.contrib.auth import (
    authenticate, 
    login as logIn,
    logout,
)

def login_page(request):
    # redirect if user is alredy logged in
    if request.user.is_authenticated:
        return redirect('/admin')

    # login logic for base users
    if (request.method == 'POST') and ('username' in request.POST) and ('phone' in request.POST):

        melli_code = request.POST.get('username')
        phone = request.POST.get('phone')
        
        user = authenticate(request, username=melli_code, password=str(phone))

        if user:
            logIn(request, user)
            return redirect('/admin')
        else:
            raise Http404('user not found')

    context = {}
    return render(request, 'login.html', context)

def log_out(request:HttpRequest):
    
    User_info_Deleter.delete_user_all_related_tables(request)
    logout(request)
    
    response = redirect(request.META.get('HTTP_REFERER'))
    for cookie in request.COOKIES:
        response.delete_cookie(cookie)
    return response