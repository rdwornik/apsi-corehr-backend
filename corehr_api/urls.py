from django.urls import path, include

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from corehr_api import views

app_name = 'corehr_api'

urlpatterns = [

]