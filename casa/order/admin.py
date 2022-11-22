from django.contrib import admin
from .models import OrderGeneration, Product,Surface,Size, Thickness, Collection 
# Register your models here.


@admin.register(Collection)
@admin.register(Thickness)
@admin.register(Size)
@admin.register(Surface)
@admin.register(Product)
@admin.register(OrderGeneration)



class OrderAdmin(admin.ModelAdmin):
    pass