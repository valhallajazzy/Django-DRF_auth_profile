from django.urls import reverse

from django.shortcuts import render, redirect
import requests
from environs import Env

env = Env()
env.read_env()

def get_profile(request, id):
    return render(request, 'profile.html', {"id": 1})


def get_sign_in(request):
    if request.method == 'GET':
        return render(request, 'sign_in.html', {})
    if request.method == 'POST':
        api_url = f"http://{env('API_URL_DOMAIN')}/api/auth/"
        phone_number = {"phone_number": f"{request.POST['phone_number']}"}
        requests.post(api_url, verify=False, json=phone_number)
        return redirect('conf_code', number=request.POST['phone_number'])


def get_confirm_code(request, number):
    context = {'phone_number': number}
    return render(request, 'code.html', context=context)
