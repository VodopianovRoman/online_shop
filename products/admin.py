from django.contrib import admin
from .models import *


# Register your models here.


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 0


class ReviewsInline(admin.TabularInline):
    model = Reviews
    extra = 0


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
    list_display = [field.name for field in Product._meta.fields]
    list_display_links = ('id', 'name')
    list_filter = ('id', 'name',)
    search_fields = ('id', 'name',)
    inlines = [ProductImageInline, ReviewsInline, ]


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
    list_display = [field.name for field in ProductImage._meta.fields]
    list_display_links = ('id', 'product')
    list_filter = ('id', 'product',)
    search_fields = ('id', 'product',)


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
    list_display = [field.name for field in ProductCategory._meta.fields]
    list_display_links = ('id', 'name')
    list_filter = ('id', 'name',)
    search_fields = ('id', 'name',)


@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
    list_display = [field.name for field in Reviews._meta.fields]
    list_display_links = ('id', 'review', 'product')
    list_filter = ('id', 'product',)
    search_fields = ('id', 'product',)