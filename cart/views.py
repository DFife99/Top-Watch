from django.shortcuts import render, redirect

# Create your views here.


def view_cart(request):
    context = {
        'cart': 'active'
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

    cart_context = {
                colour: {
                    'products_by_size': {
                        storage: {
                            'quantity': quantity}
                    }
                }
            }

    #print('cart list:')
    #print(list(cart.keys()))

    if item_id in list(cart.keys()):
        current_cart = request.session['cart'].values()
        #print('current_cart:')
        #print(current_cart)
        #print('colour:')
        print(storage)
        print('list:')
        print(list(cart.values()))
        if colour in list(cart[item_id]):
            print('PASSED 1ST IF')
            print(list(cart[item_id][colour]['products_by_size']))
            if storage in list(cart[item_id][colour]['products_by_size']):
                print('PASSED 2ND IF')
                cart[item_id][colour]['products_by_size'].update(
                    {storage: quantity+1})
            else:
                cart[item_id][colour]['products_by_size'].update(
                    {storage: quantity})

        else:
            cart[item_id].update(
                {colour: {'products_by_size': {storage: quantity}}})
    else:
        cart[item_id] = {
                    colour: {
                        'products_by_size': {
                            storage: {
                                'quantity': quantity}
                        }
                    }
                }

    request.session['cart'] = cart

    print('tesing:')
    print(request.session['cart'])

    return redirect(redirect_url)
