from django.contrib import admin

from .models import Candy, Customer, Category, Order, OrderItem


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone', 'address')
    ordering = ('first_name',)
    search_fields = ('first_name',)
    list_filter = ('email',)


admin.site.register(Category)
admin.site.register(Candy)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Order)
admin.site.register(OrderItem)
