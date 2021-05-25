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

def signup(request:HttpRequest):
    
    pre_form = MyBaseUserModelForm()

    if request.method == 'POST':
        pre_form = MyBaseUserModelForm(request.POST)
        
        if pre_form.is_valid():
            
            # save melli_code, phone, two factor code to database
            pre_form.save()
        
            response = redirect('phone_number_validate_page')
            response.set_cookie(key='melli_code', value=pre_form.cleaned_data.get('melli_code').strip(), max_age=1800)
            response.set_cookie(key='phone', value=pre_form.cleaned_data.get('phone').strip(), max_age=1800)
            
            return  response

        else: 
            print('try again . . . <signupView - form not valid>')
            print(pre_form)
            print('try again . . . <signupView - form not valid>')
            
            
    context = {
        'form' : pre_form
    }
    return render(request, 'signup.html', context)


def phone_number_validate(request:HttpRequest):

    
    if (request.method == 'POST') and ('two_factor_code' in request.POST):

        user_input = request.POST.get('two_factor_code')
        user_base_object = MyBaseUser.objects.get(melli_code=request.COOKIES['melli_code'])
        two_factor = user_base_object.two_factor_code

        if str(user_input).strip() == str(two_factor).strip():
        
            user_base_object.is_good_to_go = True
            user_base_object.save()

            return redirect('personal_info_page')


    
    context = {
        # 'client_phone' : MyBaseUser.objects.get(melli_code=request.user.username).phone
    }
    
    return render(request, 'pre_validate.html', context)