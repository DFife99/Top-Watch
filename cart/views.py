from django.shortcuts import render, redirect

# Create your views here.


def view_cart(request):
    context = {
        'cart': 'active',
        'cart_items': request.session['cart'],
    }

    print(request.session['cart'])

    return render(request, 'cart/cart.html', context)


def add_to_cart(request, item_id):
    redirect_url = request.POST.get('redirect_url')
    quantity = int(request.POST.get('quantity'))

    colour = None
    storage = None

    if 'product_colour' in request.POST:
        colour = request.POST['product_colour']

    if 'storage_cap' in request.POST:
        storage = request.POST['storage_cap']

    cart = request.session.get('cart', {})

    print(cart)
    print(request.POST)
    print(storage)
    print(colour)

    if colour:
        if item_id in list(cart):
            print('testing:' + cart[item_id][0])
            if list(cart[item_id][0]) == colour:
                print('testing:' + colour)
                cart[item_id][2] + 1
            else:
                cart[item_id][colour, storage, quantity]
        else:
            cart[item_id][colour, storage, quantity]

    request.session['cart'] = cart

    print(request.session['cart'])

    return redirect(redirect_url)
