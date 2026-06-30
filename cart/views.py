from django.shortcuts import redirect, get_object_or_404
from products.models import Product

def add_to_cart(request, product_id):

    # Check if product exists
    product = get_object_or_404(Product, id=product_id)

    # Get cart from session
    cart = request.session.get('cart', {})

    # Convert product ID to string
    product_id = str(product_id)

    # If product already exists in cart
    if product_id in cart:
        cart[product_id] += 1

    # Otherwise add it with quantity 1
    else:
        cart[product_id] = 1

    # Save updated cart back to session
    request.session['cart'] = cart

    return redirect('home')