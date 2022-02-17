from django.shortcuts import render
from django.contrib import messages
from django.core.paginator import Paginator
from .forms import ContactForm
from .models import Blog, Product, Department, Country
from django.core.exceptions import PermissionDenied
from .generic import get_or_none
from django.db.models import Q


def shop(request):
    departments = Department.objects.all()
    countries = Country.objects.all()

    context = {
        'departments': departments,
        'countries': countries
    }

    return render(request, 'webshop/shop.html', context)


def product_details(request, code):
    product = Product.objects.get(code=code)
    return render(request, 'webshop/product-details.html', {'product': product})


def about(request):
    return render(request, 'webshop/about.html', {})


def blog(request):
    blogs = Blog.objects.all().order_by('-date')

    paginator = Paginator(blogs, 6)  # shows 6 blogs per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
    }

    return render(request, 'webshop/blog.html', context)


def blog_details(request, pk):
    blog = get_or_none(Blog, pk=pk)
    return render(request, 'webshop/blog-details.html', {'blog': blog})


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            name = request.POST['name']
            messages.success(request, messages.SUCCESS)
            return render(request, 'webshop/contact.html', {'name': name})
        # otherwise display error message to the user
        messages.error(request, messages.ERROR)
        return render(request, 'webshop/contact.html', {'name': None})

    return render(request, 'webshop/contact.html', {})


def search(request):
    """displays search results via AJAX"""
    if request.method == 'GET':
        query = request.GET.get('query')
        order = request.GET.get('order')
        page_number = request.GET.get('page')

        if query:
            products = Product.objects.filter(Q(name__iexact=query) | Q(code__iexact=query))
        else:
            products = Product.objects.all().order_by('price')

        products = products.order_by(order)

        paginator = Paginator(products, 6)
        page_obj = paginator.get_page(page_number)

        return render(request, 'webshop/ajax/grid.html', {'page_obj': page_obj})

    raise PermissionDenied
