from django.urls import path, re_path
from django.conf.urls import include
from django.urls import URLPattern

from Login.views import LoginAuth

urlpatterns= [
    re_path(r'^', LoginAuth.as_view()),
]