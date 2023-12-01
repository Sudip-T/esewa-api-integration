from django.urls import path
from .views import *


app_name = 'myapp'

urlpatterns = [
    path('',home, name="home"),
    # path('esewa-payment/',AsyncView.as_view()),
    # path('verify-esewa-payment/',esewaPaymentVerification, name="verify-esewa-payment"),
    path('khalti-payment/',khaltipayment, name="khalti-payment"),
    path('verify-khalti-payment/',khaltiPaymentVerification, name="verify-khalti-payment"),
]