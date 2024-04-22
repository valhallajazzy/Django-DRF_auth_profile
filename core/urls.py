
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include('profile_front.urls')),
    path('api/', include('profile_api.urls')),
]
