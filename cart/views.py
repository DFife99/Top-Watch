import json
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib import messages

from products.models import Product, Category

# Create your views here.


def view_cart(request):

    context = {
        'hi':'hi'
    }

    return render(request, 'cart/cart.html', context)


def remove_from_cart(request):

    item_id = request.POST['item_id']
    colour = request.POST['product_colour']
    unfriendly_colour = request.POST['unfriendly_colour']
    storage = request.POST['storage']
    cart = request.session.get('cart')

    # checks to see if there is more than one colour under the item id currently in the cart
    if len(cart[item_id]['products_by_colour']) > 1:
        # checks to see if there is more than one storage under the colour currently in the cart
        print('First If')
        if len(cart[item_id]['products_by_colour'][colour]['unfriendly_colour'][unfriendly_colour]['products_by_size']) > 1:
            # if there is more than different type of storage amount, it will only remove the selected one
            del cart[item_id]['products_by_colour'][colour]['unfriendly_colour'][unfriendly_colour]['products_by_size'][storage]
            print('Second If')
        else: 
            # if there is only one storage amount, it will remove the selected colour
            print('First Else')
            del cart[item_id]['products_by_colour'][colour]
    else:
        # if there is only one colour under the id, it will check to see if there is multiple storage sizes chosen
        if len(cart[item_id]['products_by_colour'][colour]['unfriendly_colour'][unfriendly_colour]['products_by_size']) > 1:
            print('Third If')
            del cart[item_id]['products_by_colour'][colour]['unfriendly_colour'][unfriendly_colour]['products_by_size'][storage]
        # if there is only one storage under the one colour it will remove the id entirelty from the cart
        else: 
            print('Second Else')
            cart.pop(item_id)

    messages.success(request, 'Product Removed Successfully!')
    request.session['cart'] = cart
    return redirect(reverse('cart'))

def add_to_cart(request, item_id):
    # Taking variables from the html form
    redirect_url = request.POST.get('redirect_url')
    quantity = int(request.POST.get('quantity'))

    item_id = request.POST.get('product-id')

    colour = request.POST['product_colour']

    unfriendly_colour = request.POST['unfriendly_colour']

    storage = request.POST['storage_cap']

    # Creating a new cart or retrieving the current one
    cart = request.session.get('cart', {})

    # Checking to see if the ITEM ID is already in the cart
    if item_id in list(cart.keys()):
        # Checking to see if the COLOUR is already in the cart
        # under a product with the same ID
        if colour in list(cart[item_id]['products_by_colour']):
            # Checking to see if the STROAGE is already in the cart
            # under a product with the same ID and COLOUR
            print(storage)
            if storage in list(
                cart[item_id]['products_by_colour'][colour]['unfriendly_colour'][unfriendly_colour]['products_by_size']):

                # If everything being added to the cart is already there
                # the QUANTITY for that ITEM will be increased
                cart[item_id]['products_by_colour'][colour]['unfriendly_colour'][unfriendly_colour]['products_by_size'].update(
                    {storage: quantity + 1}) 
                print(cart[item_id]['products_by_colour'][colour]['unfriendly_colour'][unfriendly_colour]['products_by_size'])
            else:

                # If the storage is different to those already in the cart
                # it will create a second storage key with the quantity of 1
                cart[item_id]['products_by_colour'][colour]['unfriendly_colour'][unfriendly_colour]['products_by_size'].update(
                    {storage: quantity})

        else:
            # If the colour is different to those already in the cart
            # it will create another colour key and include the storage
            # and the quantity of 1
            cart[item_id]['products_by_colour'].update({
                colour: 
                {'unfriendly_colour': 
                    { unfriendly_colour: 
                        {'products_by_size': 
                            {storage: quantity}
                        }
                    }
                }
            })
    else:
        # If the item id isnt in the cart at all, it will create a new
        # Dictionary for the new item
        cart[item_id] = {
                'products_by_colour': {
                    colour: {
                        'unfriendly_colour': {
                            unfriendly_colour: {
                                'products_by_size': {
                                    storage: quantity
                                }
                            }
                        }
                    }
                }
            }

    # This will change the cart to refelct the added items
    request.session['cart'] = cart

    return redirect(redirect_url)
