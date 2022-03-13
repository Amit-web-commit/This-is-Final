from django.contrib import admin
from .models import *
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("productName",)}
admin.site.register(ReviewRating)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['comment', 'rate', 'review']
admin.site.register(Product, ProductAdmin)
admin.site.register(ComboPackage)
admin.site.register(Team)
admin.site.register(Customer)
admin.site.register(CustomerProfile)
admin.site.register(LocalProduct)
admin.site.register(SpecialProduct)
admin.site.register(Contact)
