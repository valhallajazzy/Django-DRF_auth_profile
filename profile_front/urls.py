from django.urls import path, include
from .views import get_sign_in, get_profile, get_confirm_code

urlpatterns = [
    path('', get_sign_in, name='auth'),
    path('conf_code/<str:number>', get_confirm_code, name='conf_code'),
    path('profile/<int:id>', get_profile, name='profile'),
]