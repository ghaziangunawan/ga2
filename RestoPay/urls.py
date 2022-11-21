# TODO: Implement Routings Herefrom django.urls import path
from RestoPay.views import show_restopay, show_withdraw
from django.urls import path

app_name = 'restopay'

urlpatterns = [
    path('', show_restopay, name='show_todolist'),
    path('withdraw/', show_withdraw, name='show_withdraw'),
]

