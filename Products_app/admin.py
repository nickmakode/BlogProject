from django.contrib import admin

# Register your models here.
from .models import Product

class adminProdct(admin.ModelAdmin):
    list_display=['name','weight_in_Kg','price','created_at','updated_at']

    def weight_in_Kg(self, obj):
        
        return '%.2f Kg' % obj.weight

admin.site.register(Product,adminProdct)