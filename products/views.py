from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
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
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))

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

    current_brand = request.session.get('current_brand')
    category = request.session.get('category')
    query = request.session.get('query')

    context = {
        'product': products,
        'current_brand': current_brand,
        'category': category,
        'query': query,
    }

    return render(request, 'products/product_detail.html', context)
