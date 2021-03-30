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
        for key, value in value.items():
            colour_str = str(value.keys()).split("'")
            colour = colour_str[1]
            for key, value in value.items():
                storage_str = str(
                    value['products_by_size'].keys()).split("'")
                storage = storage_str[1]
                quantity_str = str(
                    value['products_by_size'].values()).split("'")
                quantity = quantity_str[1]

                cart_item = {
                    'product': product,
                    'colour': colour,
                    'storage': storage,
                    'quantity': quantity
                }

                cart_items.append(cart_item)

    context = {
        'cart_items': cart_items,
        'total': total,
        'product_count': product_count
    }

    return context
