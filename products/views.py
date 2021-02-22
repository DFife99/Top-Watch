from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Product, Category

# Create your views here.


def all_products(request):
    """ a view to return all_products.html, including sorting and searching """

    products = Product.objects.all()
    query = None
    sort = None
    direction = None
    category = 'phones,tablets,smart_watches,wireless_headphones'
    current_brand = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

    current_sorting = f'{sort}_{direction}'

    if 'category' in request.GET:
        category = request.GET['category']
        categories = request.GET['category'].split(',')
        products = products.filter(category__name__in=categories)
        categories = Category.objects.filter(name__in=categories)

    if request.GET:
        if 'brand' in request.GET:
            brands = request.GET['brand'].split(',')
            products = products.filter(brand__in=brands)
            current_brand = request.GET['brand']

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            queries = Q(name__icontains=query) | Q(brand__icontains=query) | Q(
                category__name__icontains=query)
            products = products.filter(queries)

    context = {
        'products': products,
        'category': category,
        'current_brand': current_brand,
        'query': query,
    }

    request.session['current_brand'] = current_brand
    request.session['current_sorting'] = current_sorting
    request.session['category'] = category
    request.session['query'] = query

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ a view to return a specific product details """

    if request.POST:
        cart_product_id = request.POST['product-id']
        cart_product_storage = request.POST['storage_cap']
        cart_product_colour = request.POST['product_colour']

    products = get_object_or_404(Product, pk=product_id)
    storage_1 = None
    storage_2 = None
    storage_3 = None
    hex_1 = None
    hex_2 = None
    hex_3 = None
    hex_4 = None
    hex_5 = None
    hex_6 = None
    colour_1 = None
    colour_2 = None
    colour_3 = None
    colour_4 = None
    colour_5 = None
    colour_6 = None

    storage_cap = products.storage_cap

    storage_1 = storage_cap

    if "/" in storage_cap:
        storage_split = storage_cap.split('/')
        storage_1 = storage_split[0]
        storage_2 = storage_split[1]
        if len(storage_split) == 3:
            storage_3 = storage_split[2]

    hex_colour = products.hex_colour

    hex_1 = hex_colour

    if "/" in hex_colour:
        hex_split = hex_colour.split('/')
        hex_1 = hex_split[0]
        hex_2 = hex_split[1]

        if len(hex_split) >= 3:
            hex_3 = hex_split[2]

        if len(hex_split) >= 4:
            hex_4 = hex_split[3]

        if len(hex_split) >= 5:
            hex_5 = hex_split[4]

        if len(hex_split) >= 6:
            hex_6 = hex_split[5]

    colour = products.colour

    colour_1 = colour

    if "/" in colour:
        colour_split = colour.split('/')
        colour_1 = colour_split[0]
        colour_2 = colour_split[1]

        if len(colour_split) >= 3:
            colour_3 = colour_split[2]

        if len(colour_split) >= 4:
            colour_4 = colour_split[3]

        if len(colour_split) >= 5:
            colour_5 = colour_split[4]

        if len(colour_split) >= 6:
            colour_6 = colour_split[5]

    current_brand = request.session.get('current_brand')
    category = request.session.get('category')
    query = request.session.get('query')

    context = {
        'product': products,
        'current_brand': current_brand,
        'category': category,
        'query': query,
        'storage_1': storage_1,
        'storage_2': storage_2,
        'storage_3': storage_3,
        'hex_1': hex_1,
        'hex_2': hex_2,
        'hex_3': hex_3,
        'hex_4': hex_4,
        'hex_5': hex_5,
        'hex_6': hex_6,
        'colour_1': colour_1,
        'colour_2': colour_2,
        'colour_3': colour_3,
        'colour_4': colour_4,
        'colour_5': colour_5,
        'colour_6': colour_6,
    }

    return render(request, 'products/product_detail.html', context)
