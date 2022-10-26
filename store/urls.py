from django.urls import path
from django.contrib.admin.views.decorators import staff_member_required
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('products/<slug:slug>/', views.product_detail,
         name='product_detail'),
    path('add_product/', staff_member_required(views.add_product), name='add_product'),
    path('delete_product/<slug:slug>/', staff_member_required(views.delete_product),
         name='delete_product'),
    path('edit_product/<slug:slug>/', staff_member_required(views.edit_product), name='edit_product'),
]
