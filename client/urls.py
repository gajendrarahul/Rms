from django.urls import path
from . import views
urlpatterns = [
    path('clientview/',views.clientview , name='clientview')
]