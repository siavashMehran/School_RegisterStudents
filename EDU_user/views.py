from django.contrib.auth import get_user_model
from django.http.request import HttpRequest
from EDU_user.models import User_Auth_State
from EDU_user.forms import User_Auth_State_Model_Form, User_Upload_Files_Model_Form
from django.shortcuts import redirect, render
from TOOLS.QuerryDict_generator import querryDict_generator
# Create your views here.



def personal_info(request:HttpRequest):


    myUser = get_user_model().objects.filter(username=request.user.username).first()
    personal_info_form = User_Auth_State_Model_Form(initial={'user':myUser})

    if request.method == 'POST' :
        QD = querryDict_generator(request_POST=request.POST, user=myUser)
        personal_info_form = User_Auth_State_Model_Form(QD or None)

        if personal_info_form.is_valid():
            personal_info_form.save()
            return redirect('upload_page')

        else: 
            pass


    context = {
        'form' : personal_info_form
    }
    return render(request, 'personal_info.html', context)


def upload_page(request:HttpRequest):
    myUser = get_user_model().objects.filter(username=request.user.username).first()
    form = User_Upload_Files_Model_Form(initial={'user':myUser})

    if request.method == 'POST':
        QD = querryDict_generator(request.POST, user=myUser)
        form = User_Upload_Files_Model_Form(data=QD, files=request.FILES, initial={'user':myUser})
        
        if form.is_valid() : form.save() ; return redirect('verify_page')
        else : form.add_error('scan_karname', 'لطفا از اول تلاش کنید')

    context = {
        'form' : form
    }
    return render(request, 'upload.html', context)



