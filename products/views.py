from django.shortcuts import render, get_object_or_404
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

    storage_cap = products.storage_cap

    storage_1 = storage_cap

    if "/" in storage_cap:
        storage_split = storage_cap.split('/')
        storage_1 = storage_split[0]
        storage_2 = storage_split[1]
        if len(storage_split) == 3:
            storage_3 = storage_split[2]

    colour_hex = product.colour_hex

    hex_1 = colour_hex
    
    if "/" in colour_hex:
        hex_split = colour_hex.split('/')
        hex_1 = hex_split[0]
        hex_2 = hex_split[1]

        if len(hex_split) == 3:
            hex_3 = hex_split[2]
        
        if len(hex_split) == 4:
            hex_4 = hex_split[3]
        
        if len(hex_split) == 5:
            hex_5 = hex_split[4]
            
        if len(hex_split) == 6:
            hex_6 = hex_split[5]


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
    }

    return render(request, 'products/product_detail.html', context)
