from django.contrib import admin
from .models import Product, Order


# Register your models here.

# Changing the admin headers
admin.site.site_header = 'eShop administration'
admin.site.site_title = 'eShop administration'
admin.site.index_title = 'Manage eShop'


# Adding options in the admin window
class ProductAdmin(admin.ModelAdmin):
    # Defining action in the admin window. Queryset is the list of all the items inside Products.
    def change_category_to_default(self, request, queryset):
        queryset.update(category='default')

    change_category_to_default.short_description = 'Default category'
    list_display = ('title', 'price', 'category', 'description')
    search_fields = ('title', 'category', )
    actions = ("change_category_to_default",)
    list_editable = ('price',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Order)
