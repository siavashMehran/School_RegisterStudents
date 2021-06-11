from EDU_user.models import User_Auth_State, User_Upload_Files
from EDU_user.forms import User_Auth_State_Model_Form, User_Upload_Files_Model_Form
from django.shortcuts import render
from django.contrib.auth import get_user_model
# Create your views here.

def verify_page(request):
    myUser = get_user_model().objects.filter(username=request.user.username).first()

    client_upload:User_Upload_Files = User_Upload_Files.objects.get(user=myUser)
    client_info:User_Auth_State   = User_Auth_State.objects.get(user=myUser)

    client_info_form   = User_Auth_State_Model_Form(instance=client_info)

    if request.method == 'POST':
        pass

    context = {
        'scans' : client_upload,
        'form2' : client_info_form
    }
    return render(request, 'verify.html', context)