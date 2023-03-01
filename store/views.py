from django.shortcuts import get_object_or_404, render

from .models import Category, Product, ProductManager


def index(request):
    new_arrivals = Product.objects.order_by("updated")[:5]
    category = Category.objects.all()
    # products = Product.objects.filter()
    return render(request, 'store/index.html', {'category': category, 'new_arrivals': new_arrivals})


def product_all(request):
    products = Product.products.filter()
    return render(request, 'store/product_all.html', {'products': products})


def category_list(request, category_slug=None):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)
    return render(request, 'store/products/category.html', {'category': category, 'products': products})


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, in_stock=True)
    return render(request, 'store/products/single.html', {'product': product})


def contact_us(request):
    return render(request, 'store/contact-us.html')


def about(request):
    return render(request, 'store/about.html')


def blog(request):
    return render(request, 'store/blog.html')


def compare(request):
    return render(request, 'store/compare.html')


def login(request):
    return render(request, 'store/login.html')


def wishlist(request):
    return render(request, 'store/wishlist.html')


def my_account(request):
    return render(request, 'store/my-account.html')


def checkout(request):
    return render(request, 'store/checkout.html')
