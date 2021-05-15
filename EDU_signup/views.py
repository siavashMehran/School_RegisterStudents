from django.http.response import Http404
from EDU_signup.forms import MyBaseUserModelForm
from django.shortcuts import redirect, render
from django.http import HttpRequest
# Create your views here.


def home(request:HttpRequest):

    pre_form = MyBaseUserModelForm(request.POST)

    if request.method == 'POST':
        
        if pre_form.is_valid():
            pre_form.save()
            return redirect('pre_validate')
            
        else: raise Http404('form is not valid') 

    context = {
        'form' : pre_form
    }

    return render(request, 'index.html', context)


def pre_validate(request:HttpRequest):

    if request.method == 'POST'
    context = {}

    return render(request, 'pre_validate.html', context)