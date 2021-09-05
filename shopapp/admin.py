from django.contrib import admin
from . models import *
# Register your models here.

class catadmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    list_display = ['name','slug']
admin.site.register(catag,catadmin)
class prdadmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    list_display = ['name', 'slug','price','stock','img','available']
    list_editable = ['available','stock','price', 'stock','img']
admin.site.register(product,prdadmin)
