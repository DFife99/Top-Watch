from django.shortcuts import render

# Create your views here.


def index(request):
    context = {
        'index': 'active'
    }
    return render(request, 'home/index.html', context)
