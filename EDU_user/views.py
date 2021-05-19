from django.contrib.auth import get_user_model
from django.http.request import HttpRequest
from EDU_user.models import User_Auth_State
from EDU_user.forms import User_Auth_State_Model_Form
from django.shortcuts import redirect, render

# Create your views here.



def personal_info(request:HttpRequest):

    if User_Auth_State.objects.filter(user=request.user):
        redirect('/')

    myUser = get_user_model().objects.filter(username=request.user.username).first()
    personal_info_form = User_Auth_State_Model_Form(initial={'user':myUser})
    

    if request.method == 'POST' :
        personal_info_form = User_Auth_State_Model_Form(request.POST)
        if personal_info_form.is_valid():
            personal_info_form.save()
        else:
            personal_info_form:User_Auth_State_Model_Form.add_error(error='asd')


    context = {
        'form' : personal_info_form
    }
    return render(request, 'personal_info.html', context)