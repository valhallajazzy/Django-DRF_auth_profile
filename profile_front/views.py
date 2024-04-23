from django.urls import reverse

from django.shortcuts import render, redirect
import requests
from environs import Env

env = Env()
env.read_env()


def get_profile(request, phone_number):
    if request.method == "GET":
        api_url = f"http://{env('API_URL_DOMAIN')}/api/get_profile/"
        phone_number = {"phone_number": phone_number}
        response = requests.post(api_url, verify=False, json=phone_number)
        if 'personal_data' in response.json():
            return render(request, 'profile.html', response.json()['personal_data'])
        return render(request, 'profile.html', {})

    if request.method == "POST":
        api_url = f"http://{env('API_URL_DOMAIN')}/api/invite_code/"
        request_data = {"phone_number": phone_number,
                        "friend_invite_code": f"{request.POST['friend_invite_code']}"}
        requests.post(api_url, verify=False, json=request_data)
        return redirect('profile', phone_number=phone_number)


def sign_in(request):
    if request.method == 'GET':
        return render(request, 'sign_in.html', {})
    if request.method == 'POST':
        api_url = f"http://{env('API_URL_DOMAIN')}/api/sign_in/"
        phone_number = {"phone_number": f"{request.POST['phone_number']}"}
        requests.post(api_url, verify=False, json=phone_number)
        return redirect('conf_code', phone_number=request.POST['phone_number'])


def sign_up(request, phone_number):
    if request.method == 'GET':
        context = {'phone_number': phone_number}
        return render(request, 'code.html', context=context)

    if request.method == 'POST':
        api_url = f"http://{env('API_URL_DOMAIN')}/api/sign_up/"
        request_data = {"phone_number": phone_number,
                        "code": int(request.POST['code'])}
        response = requests.post(api_url, verify=False, json=request_data)
        if 'is_active' not in response.json():
            return render(request, 'code.html', {})
        return redirect('profile', phone_number=phone_number)


def logout(request, phone_number):
    api_url = f"http://{env('API_URL_DOMAIN')}/api/logout/"
    phone_number = {"phone_number": phone_number}
    requests.post(api_url, verify=False, json=phone_number)
    return redirect('sign_in')
