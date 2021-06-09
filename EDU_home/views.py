from django.shortcuts import redirect, render

# Create your views here.

def home(request):
    if request.user.is_authenticated:
        return redirect('logout_page')

    context = {}
    return render(request, 'index.html', context)