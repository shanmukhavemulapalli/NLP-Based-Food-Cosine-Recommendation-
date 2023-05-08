from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(userInfo)
class userInfo(admin.ModelAdmin):
    pass


@admin.register(Order)
class Order(admin.ModelAdmin):
    pass
