import json
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib import messages

from products.models import Product, Category

# Create your views here.


def view_cart(request):

    return render(request, 'cart/cart.html')


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
        # Checking to see if the COLOUR is already in the cart under a product with the same ID
        if colour in list(cart[item_id]['products_by_colour']):
            # Checking to see if the STROAGE is already in the cart under a product with the same ID and COLOUR
            if storage in list(
                cart[item_id]['products_by_colour'][colour]['unfriendly_colour'][unfriendly_colour]['products_by_size']):
                # If everything being added to the cart is already there the QUANTITY for that ITEM will be increased
                
                # Gets the quantity of the product currently in the cart
                original_quantity = int(cart[item_id]['products_by_colour'][colour]['unfriendly_colour'][unfriendly_colour]['products_by_size'][storage])

                # Navigates to the quantity of the item in the cart, and adds the new quantity with the original quantity
                cart[item_id]['products_by_colour'][colour]['unfriendly_colour'][unfriendly_colour]['products_by_size'].update(
                    {storage: original_quantity + quantity})
            else:

                # If the storage is different to those already in the cart it will create a second storage key with the quantity of 1
                cart[item_id]['products_by_colour'][colour]['unfriendly_colour'][unfriendly_colour]['products_by_size'].update(
                    {storage: quantity})

        else:
            # If the colour is different to those already in the cart it will create another colour key and include the storage and the quantity of 1
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
        # If the item id isnt in the cart at all, it will create a new dictionary for the new item
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
    messages.success(request, 'Product Added To Your Cart!')

    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    bag = request.session.get('bag', {})

    if size:
        if quantity > 0:
            bag[item_id]['items_by_size'][size] = quantity
            messages.success(request,
                (f'Updated size {size.upper()} '
                f'{product.name} quantity to '
                f'{bag[item_id]["items_by_size"][size]}'))
        else:
            del bag[item_id]['items_by_size'][size]
            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)
                messages.success(request,
                    (f'Removed size {size.upper()} '
                    f'{product.name} from your bag'))
    else:
        if quantity > 0:
            bag[item_id] = quantity
            messages.success(request,
                (f'Updated {product.name} '
                f'quantity to {bag[item_id]}'))
        else:
            bag.pop(item_id)
            messages.success(request,
                (f'Removed {product.name} '
                f'from your bag'))

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))

def remove_from_cart(request):

    # Taking items from the html form
    item_id = request.POST['item_id']
    colour = request.POST['product_colour']
    unfriendly_colour = request.POST['unfriendly_colour']
    storage = request.POST['storage']
    cart = request.session.get('cart')

    # checks to see if there is more than one colour under the item id currently in the cart
    if len(cart[item_id]['products_by_colour']) > 1:

        # checks to see if there is more than one storage under the colour currently in the cart
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

            # If there is multiple storage sizes it will only remove the selected one
            del cart[item_id]['products_by_colour'][colour]['unfriendly_colour'][unfriendly_colour]['products_by_size'][storage]

        # if there is only one storage under the one colour it will remove the id entirelty from the cart
        else: 
            cart.pop(item_id)

    # Sends a message to the html to allow the user to know theyve been successful
    messages.success(request, 'Product Removed Successfully!')

    # Updates the cart without the item that was removed
    request.session['cart'] = cart
    return redirect(reverse('cart'))


def clear_cart(request):
    cart = request.session.get('cart')
    cart.clear()
    request.session['cart'] = cart
    messages.success(request, 'Cart Cleared Successfully!')
    return redirect(reverse('cart'))
