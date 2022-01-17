from django.db import models

# Create your models here.

# Inheriting from models.Model
# Name is a characther field that represents the programmatic name (eg. bed_bath)
# The length of the programmatic name will be a max length of 254 characters long
# A friendly name (eg. Bed & Bath) which will make that name a little more friendly looking for the Frontend
# null and blank = True means that the friendly name is optional
class Category(models.Model):
    
    # Fixing the spelling issue on category model by adding a metaclass to the category model.
    # A Meta class (class Meta:) is a subclass of a Class....
    class Meta:
        # variable name for changing the spelling error to correct spelling
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    # Takes in the category model (above) itself.
    # And simply returns self.name
    # Basically this returns the Category Name
    def __str__(self):
        return self.name

    # A quick model method same as the string method (above) but will return "friendly_name" if I want it.
    def get_friendly_name(self):
        return self.friendly_name


# The first field is a "foreign key" to the category model.
# It's being allowed null in the database and blank in forms
# and if a category is deleted I'll set any products that use it to have null for this field
# rather than deleting the product
# Each product has a SKU, NAME, DESCRIPTION
class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
    # Will return the products name
