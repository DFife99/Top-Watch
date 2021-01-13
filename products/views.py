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

            queries = Q(name__icontains=query) | Q(brand__icontains=query) | Q(category__name__icontains=query)
            products = products.filter(queries)

    context = {
        'products': products,
        'category': category,
        'current_sorting': current_sorting,
        'current_brand': current_brand
    }

    return render(request, 'products/products.html', context)
