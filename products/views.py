from django.shortcuts import render
from .models import Product, Category


def home(request):

    # Get all categories
    categories = Category.objects.all()

    # Get category from URL
    category_id = request.GET.get('category')

    # Get search text from URL
    search = request.GET.get('search')

    # Start with all products
    products = Product.objects.all()

    # Filter by category
    if category_id:
        products = products.filter(category_id=category_id)

    # Filter by search text
    if search:
        products = products.filter(name__icontains=search)

    return render(request, 'home.html', {
        'products': products,
        'categories': categories,
    })