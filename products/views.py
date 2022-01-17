from django.shortcuts import render
from .models import Product
# Create your views here.

def all_products(request):
    """ A view to show all products, including sorting and search queries """

    # Return all products from the database using: product.objects.all()
    products = Product.objects.all()

    # Context so that the products will be available in the template
    context = {
        'products': products,
    }

    # This is retruning the product webpage
                # Context is for when I need to send some things back to the template
    return render(request, 'products/products.html', context)