from django.contrib import admin
from libreria.models import Books, Bindings, Personalnotebook

# Register your models here.

@admin.register(Books)
class Books_admin(admin.ModelAdmin):

    list_display = ['name',  'price',  'author',  'is_active', 'book_is_atp',  'book_category',  'stock' ]

@admin.register(Bindings)
class Bindings_admin(admin.ModelAdmin):

    list_display= ["name", "price","bind_size","book_is_hardcover", "colorbook"]

@admin.register(Personalnotebook)
class Personalnotebook(admin.ModelAdmin):

    list_display= ["name", "price","bind_size","book_is_hardcover", "colorbook"]
