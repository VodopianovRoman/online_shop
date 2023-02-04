from django.contrib import admin
from .models import *

# Register your models here.


@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
    list_display = ('id', 'email', 'name')
    list_display_links = ('id', 'email')
    list_filter = ('email', )
    search_fields = ('id', 'email')