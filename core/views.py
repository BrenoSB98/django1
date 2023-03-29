from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.template import loader

from .models import Product


def index(request):
    products = Product.objects.all()

    context = {
        'course': 'Programation Web with Django Framework',
        'other': 'Django is fine!',
        'products': products
    }
    return render(request, 'index.html', context)


def contact(request):
    return render(request, 'contact.html')


def product(request, pk):
    prod = get_object_or_404(Product, id=pk)

    context = {
        'product': prod
    }
    return render(request, 'product.html', context)


def error404(request, ex):
    template = loader.get_template('404.html')
    return HttpResponse(content=template.render(),
                        content_type='text/thml; charset=utf8', status=404)


def error500(request):
    template = loader.get_template('500.html')
    return HttpResponse(content=template.render(),
                        content_type='text/html; charset=utf8', status=500)
