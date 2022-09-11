from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home')
]

handler404 = 'store.views.handler404'
