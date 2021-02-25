from django.shortcuts import render, redirect

# Create your views here.


def view_cart(request):

    context = {
        'cart': 'active'
    }
    print(request.session['cart'])

    return render(request, 'cart/cart.html', context)


def add_to_cart(request, item_id):
    # Taking variables from the html form
    redirect_url = request.POST.get('redirect_url')
    quantity = int(request.POST.get('quantity'))

    colour = request.POST['product_colour']
    storage = request.POST['storage_cap']

    # Creating a new cart or retrieving the current one
    cart = request.session.get('cart', {})

    # Checking to see if the ITEM ID is already in the cart
    if item_id in list(cart.keys()):

        # Checking to see if the COLOUR is already in the cart
        # under a product with the same ID
        if colour in list(cart[item_id]):

            # Checking to see if the STROAGE is already in the cart
            # under a product with the same ID and COLOUR
            if storage in list(cart[item_id][colour]['products_by_size']):

                # If everything being added to the cart is already there
                # the QUANTITY for that ITEM will be increased
                cart[item_id][colour]['products_by_size'].update(
                    {storage: quantity+1})
            else:

                # If the storage is different to those already in the cart
                # it will create a second storage key with the quantity of 1
                cart[item_id][colour]['products_by_size'].update(
                    {storage: quantity})

        else:

            # If the colour is different to those already in the cart
            # it will create another colour key and include the storage
            # and the quantity of 1
            cart[item_id].update(
                {colour: {'products_by_size': {storage: quantity}}})
    else:

        # If the item id isnt in the cart at all, it will create a new
        # Dictionary for the new item
        cart[item_id] = {
                    colour: {
                        'products_by_size': {
                            storage: quantity
                        }
                    }
                }

    # This will change the cart to refelct the added items
    request.session['cart'] = cart

    print('tesing:')
    print(request.session['cart'])

    return redirect(redirect_url)
