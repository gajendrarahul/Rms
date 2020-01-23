from django.urls import path
from django.conf.urls import url
from . import views
from django.contrib.auth.views import PasswordResetView,PasswordResetDoneView,PasswordResetConfirmView,PasswordResetCompleteView
urlpatterns = [
    path('OwnerAccountCreate/',views.OwnerAccountCreate, name='OwnerAccountCreate'),
    path('ClientAccountCreate/',views.ClientAccountCreate, name='ClientAccountCreate'),




]