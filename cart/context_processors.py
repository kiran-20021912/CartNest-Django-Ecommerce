def cart_count(request):

    # Get cart from session
    cart = request.session.get('cart', {})

    # Calculate total quantity
    total_items = sum(cart.values())

    return {
        'cart_count': total_items
    }