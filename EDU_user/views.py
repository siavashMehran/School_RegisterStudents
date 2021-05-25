from django.contrib.auth import get_user_model
from django.http.request import HttpRequest
from EDU_user.models import User_Auth_State
from EDU_user.forms import User_Auth_State_Model_Form
from django.shortcuts import redirect, render

# Create your views here.



def personal_info(request:HttpRequest):


    myUser = get_user_model().objects.filter(username=request.user.username).first()
    personal_info_form = User_Auth_State_Model_Form()
    

    if request.method == 'POST' :
        personal_info_form = User_Auth_State_Model_Form(request.POST, initial={'user':myUser})
        personal_info_form:User_Auth_State_Model_Form.fields.get('user') = request.user
        if personal_info_form.is_valid():
            personal_info_form.save()
        else:
            personal_info_form:User_Auth_State_Model_Form.add_error(error='asd')


    context = {
        'form' : personal_info_form
    }
    return render(request, 'personal_info.html', context)