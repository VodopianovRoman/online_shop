from django.contrib import admin
from .models import *


# Register your models here.


class ProductInOrderInline(admin.TabularInline):
    model = ProductInOrder
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
    list_display = [field.name for field in Order._meta.fields]
    # list_display = ('id', 'customer_name', 'customer_email', 'customer_phone', 'address', 'total_price',
    #                 'comments', 'status', 'created', 'updated')
    list_display_links = ('id', 'customer_name')
    list_filter = ('id', 'customer_email', 'customer_phone')
    search_fields = ('id', 'customer_email', 'customer_phone')
    inlines = [ProductInOrderInline, ]


@admin.register(Status)
class StatusOrder(admin.ModelAdmin):
    empty_value_display = '-empty-'
    list_display = [field.name for field in Status._meta.fields]
    list_display_links = ('id', 'name')
    list_filter = ('name',)


@admin.register(ProductInOrder)
class ProductInOrderAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
    list_display = [field.name for field in ProductInOrder._meta.fields]
    list_display_links = ('id', 'order', 'product',)
    list_filter = ('id', 'order', 'product',)


@admin.register(ProductInBasket)
class ProductInBasketAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
    list_display = [field.name for field in ProductInBasket._meta.fields]
    list_display_links = ('id', 'order', 'product',)
    list_filter = ('id', 'order', 'product',)
