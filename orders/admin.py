from django.contrib import admin
from orders.models import Order, Item, ItemOrder, Discount, Category


class ItemOrderInline(admin.TabularInline):
    model = ItemOrder
    extra = 1


class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'discountstring', 'description')


class OrderAdmin(admin.ModelAdmin):
    inlines = (ItemOrderInline, )
    list_display = ('name', 'itemstring', 'total', 'wiebetaaltwat')

admin.site.register(Order, OrderAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(Discount)
admin.site.register(Category)
