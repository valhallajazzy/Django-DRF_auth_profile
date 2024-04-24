from django.urls import path, include, re_path

from profile_api.views import (PhoneNumberAPIView, SignUpAPIView,
                               InviteCodeAPIView, ProfileAPIView, LogoutAPIView, GetCodeAPIView)

urlpatterns = [
    path("sign_in/", PhoneNumberAPIView.as_view()),
    path("sign_up/", SignUpAPIView.as_view()),
    path("invite_code/", InviteCodeAPIView.as_view()),
    path("get_profile/", ProfileAPIView.as_view()),
    path("logout/", LogoutAPIView.as_view()),
    path("get_users/", GetCodeAPIView.as_view())
]