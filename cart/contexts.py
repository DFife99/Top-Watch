from django.shortcuts import get_object_or_404
from products.models import Product


def cart_contents(request):

    cart_items = []
    total = 0
    product_count = 0
    cart = request.session.get('cart', {})

    for item_id, colour in cart.items():
        product = get_object_or_404(Product, pk=item_id)
        cart_items.append({
            'item_id': item_id,
            'colour': colour,
            'product': product
        })
        print(item_id)
        print(colour)

    context = {
        'cart_items': cart_items,
        'total': total,
        'product_count': product_count
    }

    print("Context:")
    print(context)
    return context
