from django.urls import path
from .views import *
# from .views import AsyncView

urlpatterns = [
    path('',home),
    path('verify-payment/',AsyncView.as_view()),
    path('success/',esewaPaymentVerification),
]