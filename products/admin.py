from django.contrib import admin
from .models import Product, Category

# Register your models here.

# Admin console under products this is the list of columns
#  Column titles from Left to Right
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image'
    )
    #  Sets the tab for sorting to 'SKU' in this case
    ordering = ('sku',)

# Sets the column title for the category page
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

    ordering = ('friendly_name',)

# Registineg the ProductAdmin & CatgoryAdmin models
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
