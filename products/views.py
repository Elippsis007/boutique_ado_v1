from django.shortcuts import render, get_object_or_404
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


def product_detail(request, product_id):
    """ A view to show all product details, including sorting and search queries """

    # Return a product from the database using: product.objects.all()
    product = get_object_or_404(Product, pk=product_id)

    # Context so that the products will be available in the template
    context = {
        'product': product,
    }

    # This is retruning the product webpage
                # Context is for when I need to send some things back to the template
    return render(request, 'products/product_detail.html', context)