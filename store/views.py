from django.shortcuts import render
from .models import Product
from category.models import Category
from django.shortcuts import get_object_or_404



def product_all(request):
    products = Product.objects.prefetch_related("product_image").filter(is_active=True)
    return render(request, 'store/products/index.html', {'products': products})


def category_list(request, category_slug=None):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(
        category__in=get_object_or_404(Category,name=category_slug).get_descendants(include_self=True)
    )
    return render(request, 'store/products/category.html', {'category': category, 'products': products})


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, is_active=True)
    return render(request, 'store/products/single.html', {'product': product})