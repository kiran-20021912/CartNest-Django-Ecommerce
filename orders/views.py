from django.shortcuts import redirect
from .models import Order, OrderItem
from products.models import Product


def place_order(request):

    # Get cart from session
    cart = request.session.get('cart', {})

    # If cart is empty
    if not cart:
        return redirect('cart_detail')

    # Get all products in cart
    products = Product.objects.filter(id__in=cart.keys())

    # Calculate total price
    total_price = 0

    for product in products:
        quantity = cart[str(product.id)]
        total_price += product.price * quantity

    # Create Order
    order = Order.objects.create(
        user=request.user,
        total_price=total_price
    )

    # Create OrderItems
    for product in products:
        quantity = cart[str(product.id)]

        OrderItem.objects.create(
            order=order,
            product=product,
            quantity=quantity,
            price=product.price
        )

    # Clear cart
    request.session['cart'] = {}

    # Redirect (we'll create this page next)
    return redirect('home')