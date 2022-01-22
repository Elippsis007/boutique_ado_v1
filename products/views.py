from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category
# Create your views here.

def all_products(request):
    """ A view to show all products, including sorting and search queries """

    # Return all products from the database using: product.objects.all()
    products = Product.objects.all()
    query = None
    categories = None

    # Getting the category parameters

    # Seeing if it exists in "if request.GET"
    if request.GET:

        if request.GET:
            # Checking to see whether sort is in "request.get"
            if 'sort' in request.GET:



        if 'category' in request.GET:
            # If it does exist it will be split into a list
            categories = request.GET['category'].split(',') 
            #  Then use the list to filter the current set of "All products" down to only the products whose category name is in the list
            #  The __ means I'm looking for the name field of the category model.
            products = products.filter(category__name__in=categories)
            # Filter all categories down to the ones whose name is in the list from the url
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query) 
            products = products.filter(queries)         

    # Context so that the products will be available in the template
    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
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