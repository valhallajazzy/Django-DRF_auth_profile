from django.urls import path, include
from .views import sign_in, get_profile, sign_up, logout

urlpatterns = [
    path('', sign_in, name='sign_in'),
    path('sign_up/<str:phone_number>', sign_up, name='conf_code'),
    path('profile/<str:phone_number>', get_profile, name='profile'),
    path('logout/<str:phone_number>', logout, name='logout')
]