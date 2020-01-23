from django.urls import path
from . import views
urlpatterns = [
    path('ownerview/',views.ownerview, name='ownerview')
]