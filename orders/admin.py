from django.contrib import admin
from orders.models import Order, Item, ItemOrder


class ItemOrderInline(admin.TabularInline):
    model = ItemOrder
    extra = 1


class OrderAdmin(admin.ModelAdmin):
    inlines = (ItemOrderInline, )
    list_display = ('name', 'itemstring', 'total', 'in_wie_betaalt_wat')

admin.site.register(Order, OrderAdmin)
admin.site.register(Item)
