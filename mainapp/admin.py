from django.contrib import admin
from .models import *
from django.forms import ModelChoiceField

admin.site.register(Category)
admin.site.register(CartProduct)
admin.site.register(Cart)
admin.site.register(Customer)