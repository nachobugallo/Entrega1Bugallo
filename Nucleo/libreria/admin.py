from django.contrib import admin
from libreria.models import Books

# Register your models here.

@admin.register(Books)
class Books_admin(admin.ModelAdmin):

    list_display = ['name',  'price',  'author',  'is_active', 'book_is_atp',  'book_category',  'stock' ]