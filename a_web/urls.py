from django.urls import path
from .views import *

urlpatterns = [
    path('', atos_inhouse, name='atos_inhouse'),
]