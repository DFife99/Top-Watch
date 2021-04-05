from django.shortcuts import get_object_or_404
from products.models import Product


def cart_contents(request):

    cart_items = []
    total = 0
    product_count = 0
    cart = request.session.get('cart', {})

    for key, value in cart.items():
        i = int(1)
        pk = key
        product = get_object_or_404(Product, pk=pk)
        for colour, value in value['products_by_colour'].items():
            for storage, quantity in value['products_by_size'].items():
                cart_item = {
                    'product': product,
                    'colour': colour,
                    'storage': storage,
                    'quantity': quantity
                }

                cart_items.append(cart_item)
                print(cart_items)

    context = {
        'cart_items': cart_items,
        'total': total,
        'product_count': product_count
    }

    return context
