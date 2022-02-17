from django.urls import path
from . import views

urlpatterns = [
    path('', views.shop, name='shop'),
    path('product-details/<str:code>', views.product_details, name='product-details'),
    path('about', views.about, name='about'),
    path('blog', views.blog, name='blog'),
    path('blog-details/<int:pk>', views.blog_details, name='blog-details'),
    path('contact', views.contact, name='contact'),
    path('search', views.search, name='search')
]