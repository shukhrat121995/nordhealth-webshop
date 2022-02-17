from django.contrib import admin
from .models import Contact, Blog, Department, Country, Product


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    list_per_page = 10


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    list_per_page = 10


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'code', 'price', 'quantity']
    search_fields = ['name', 'code']
    autocomplete_fields = ['origin', 'department']
    list_per_page = 50


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'date', 'author']
    autocomplete_fields = ['author']
    list_per_page = 50


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'message']
    list_per_page = 50
