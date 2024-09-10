from django.contrib import admin

from store.models import Cart, Category, Heri, Heritage, Order, OrderItem, Product, Profile, Tradition, tradi

# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Profile)
admin.site.register(Heritage)
admin.site.register(Heri)
admin.site.register(Tradition)
admin.site.register(tradi)