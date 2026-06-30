from django.shortcuts import render,get_object_or_404
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


def product_detail(request, product_id):

    # Get the product by ID or return 404 if it doesn't exist
    product = get_object_or_404(Product, id=product_id)

    return render(request, 'product_detail.html', {
        'product': product
    })