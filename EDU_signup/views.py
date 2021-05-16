from EDU_signup.models import MyBaseUser
from django.http.response import Http404
from EDU_signup.forms import MyBaseUserModelForm
from django.shortcuts import redirect, render
from django.http import HttpRequest
from django.db.utils import IntegrityError

# imports for making a base user

from django.contrib.auth import (
    authenticate, 
    login as logIn,
    logout, 
    get_user_model,
)

def home(request:HttpRequest):

    pre_form = MyBaseUserModelForm(request.POST or None)

    if request.method == 'POST':
        
        if pre_form.is_valid():

            # save melli_code, phone, two factor code to database
            pre_form.save()

            # create a basic user from the form and log it in
            user_model = get_user_model()
            if not user_model.objects.filter(username=pre_form.cleaned_data.get('melli_code')):
                try :  base_user = user_model.objects.create_user(username=str(pre_form.cleaned_data.get('melli_code')), password=str(pre_form.cleaned_data.get('phone')))
                except IntegrityError: raise Http404('user alredy exists')
            
            logIn(request, base_user)
        
            return redirect('pre_validate')

        else: 
            print('try again . . . <homeView - form not valid>')
            print(pre_form)
            print('try again . . . <homeView - form not valid>')
            
            
    context = {
        'form' : pre_form
    }
    return render(request, 'index.html', context)


def pre_validate(request:HttpRequest):

    print()
    print(request.COOKIES)
    print()
    if (request.method == 'POST') and ('two_factor_code' in request.POST):
        user_input = request.POST.get('two_factor_code')
        two_factor = MyBaseUser.objects.get(melli_code=request.user.get_username()).two_factor_code

        if str(user_input) == str(two_factor):
            client_base_user = MyBaseUser.objects.get(melli_code=request.user.get_username())
            client_base_user.is_good_to_go = True
            client_base_user.save()
            return redirect('/')


    client_phone = MyBaseUser.objects.get(melli_code=request.user.username)
    context = {
        
    }
    
    return render(request, 'pre_validate.html', context)