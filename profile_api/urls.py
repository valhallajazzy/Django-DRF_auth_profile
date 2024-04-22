from django.urls import path

from rest_framework.routers import SimpleRouter

from profile_api.views import PhoneNumberAPIView, SignInAPIView

router = SimpleRouter()

urlpatterns = [
    path("auth/", PhoneNumberAPIView.as_view()),
    path("sign_in/", SignInAPIView.as_view())
]