from django.contrib.auth import get_user_model
from django.http.request import HttpRequest
from EDU_user.models import User_Auth_State, User_Upload_Files
from EDU_user.forms import User_Auth_State_Model_Form, User_Upload_Files_Model_Form
from django.shortcuts import redirect, render
from django.http.response import Http404, HttpResponse
# Create your views here.



def personal_info(request:HttpRequest):


    myUser = get_user_model().objects.filter(username=request.user.username).first()
    personal_info_form = User_Auth_State_Model_Form(initial={'user':myUser})

    if request.method == 'POST' :

        personal_info_form = User_Auth_State_Model_Form(request.POST, initial={'user':myUser})
        if personal_info_form.is_valid():
            personal_info_form.save()
            return redirect('upload_page')

        else:
            personal_info_form:User_Auth_State_Model_Form.add_error(error='اطلاعات نادرست')
            print('$'*100)
            print(personal_info_form.cleaned_data.get('user'))
            print(personal_info_form.initial)
            print('$'*100)


    context = {
        'form' : personal_info_form
    }
    return render(request, 'personal_info.html', context)


def upload_page(request:HttpRequest):
    myUser = get_user_model().objects.filter(username=request.user.username).first()
    form = User_Upload_Files_Model_Form(initial={'user':myUser})
    print(form.initial)
    if request.method == 'POST':
        form = User_Upload_Files_Model_Form(data=request.POST, files=request.FILES, initial={'user':myUser})
        print()
        print(form.initial)
        print()
        print(form.data)
        print()
        print(form.files)
        print(request.FILES)
        print()
        print()
        
        if form.is_valid() : form.save() ; return redirect('verify_page')
        else : form.add_error('scan_karname', 'لطفا از اول تلاش کنید') ; print();print('%'*200);print();return redirect()

    context = {
        'form' : form
    }
    return render(request, 'upload.html', context)



