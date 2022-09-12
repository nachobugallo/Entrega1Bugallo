from django.contrib import admin
from users.models import User
# Register your models here.
@admin.register(User)
class User_admin(admin.ModelAdmin):

    list_display = ['user',  'phone',  'address',  'image' ]