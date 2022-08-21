from django.contrib.admin import ModelAdmin
from django.contrib import admin
from .models import Category, Product, Brand

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug',)
    list_filter = ('name',)
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug',)
    list_filter = ('name',)
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'category', 'brand', 'price',)
    list_filter = ('category', 'brand',)
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name', 'brand', 'category',)
