from django.shortcuts import render, redirect

# Create your views here.

def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')


# A view that takes both the request and the item_id which is the id of the product the user would like to add to the bag
def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

# Getting the quantity from the form, it has to be converted to an interger since it will come from the template as a string
    quantity = int(request.POST.get('quantity'))
# I want to get the redirect URL from the form so I know where to redirect once the process is finished
    redirect_url = request.POST.get('redirect_url')
# A session allows information to be stored until the client and server are done communicating.
# Allowing me to store the contents in the shopping bag while in the HTTP session while a user browses the site and adds
# items to be purchased, without the fear of losing all items in the bag.

# Creating a variable called bag which accesses the request session trying to get this variable if it already exists
# and initializing it to an "empty dictionary" if it doesn't
# Checking to see if there is a bag variable in the session and if not then one will be created.
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity

    request.session['bag'] = bag
    return redirect(redirect_url)