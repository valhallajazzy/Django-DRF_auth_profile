from django.shortcuts import render

# Create your views here.


def get_profile(request, id):
    return render(request, 'profile.html', {"id": 1})


def get_sign_in(request):
    return render(request, 'sign_in.html', {})


def get_confirm_code(request):
    return render(request, 'code.html', {})