from django.urls import path
from . import views
from .views import hello_view, info_view


urlpatterns = [
    path('hello/', hello_view),
    path('info/', info_view),
]