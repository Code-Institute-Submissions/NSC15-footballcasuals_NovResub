from . import views
from django.urls import path

urlpatterns = [
    path('', views.view_posts, name='posts'),
    path("<slug:slug>/", views.view_post_info, name='view_post_info'),
]