from django.shortcuts import render

# Create your views here.

def verify_page(request):

    context = {}
    return render(request, 'verify.html', context)