from django.shortcuts import render

# Create your views here.


def view_cart(request):
    context = {
        'cart': 'active'
    }

    item_id = request.session.get['cart_product_id']

    if 'cart_product_colour' in request.POST:
        colour = request.POST['product_colour']

    cart = request.session.get('cart', {})

    if colour:
        if item_id in list(cart.keys()):
            if colour in cart[item_id]['items_by_colour'].keys():
                cart[item_id]['items_by_colour'][colour]
        else:
            cart[item_id] = {
                'items_by_colour': {
                    'storage': request.session.get['cart_product_storage']
                    }
            }

    request.session['cart'] = cart
    print(request.session['cart'])

    return render(request, 'cart/cart.html', context)
