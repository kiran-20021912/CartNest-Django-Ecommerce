from django.shortcuts import redirect, get_object_or_404,render
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


def cart_detail(request):

    # Get cart from session
    cart = request.session.get('cart', {})

    # Get products from database
    products = Product.objects.filter(id__in=cart.keys())

    # List to store cart items
    cart_items = []

    # Grand total
    total_price = 0

    for product in products:

        quantity = cart[str(product.id)]

        subtotal = product.price * quantity

        total_price += subtotal

        cart_items.append({
            'product': product,
            'quantity': quantity,
            'subtotal': subtotal,
        })

    context = {
        'cart_items': cart_items,
        'total_price': total_price,
    }

    return render(request, 'cart_detail.html', context)


def increase_quantity(request, product_id):

    # Get cart from session
    cart = request.session.get('cart', {})

    # Increase quantity
    cart[str(product_id)] += 1

    # Save updated cart
    request.session['cart'] = cart

    # Redirect back to cart page
    return redirect('cart_detail')


def decrease_quantity(request, product_id):

    # Get cart from session
    cart = request.session.get('cart', {})

    # Check if product exists in cart
    if str(product_id) in cart:

        # If quantity is greater than 1, decrease it
        if cart[str(product_id)] > 1:
            cart[str(product_id)] -= 1

        # Otherwise remove the product
        else:
            del cart[str(product_id)]

    # Save updated cart
    request.session['cart'] = cart

    # Redirect back to cart page
    return redirect('cart_detail')


def remove_from_cart(request, product_id):

    cart = request.session.get('cart', {})

    if str(product_id) in cart:
        del cart[str(product_id)]

    request.session['cart'] = cart

    return redirect('cart_detail')

def empty_cart(request):

    request.session['cart'] = {}

    return redirect('cart_detail')