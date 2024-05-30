from django.contrib import admin
from .models import Perfume,customer,orders
# Register your models here.

# class PerfumeAdmin(admin.ModelAdmin):
#     list_display = ('brand','price','stock')


# class CustomerAdmin(admin.ModelAdmin):
#     list_display = ('brand','price','stock')


# class OrdersAdmin(admin.ModelAdmin):
#     list_display = ('brand','price','stock')

admin.site.register(Perfume)
admin.site.register(customer)
admin.site.register(orders)

# admin.site.register(Perfume,PerfumeAdmin)
# admin.site.register(customer,CustomerAdmin)
# admin.site.register(orders,OrdersAdmin)
