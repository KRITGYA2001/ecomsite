from unicodedata import category
from django.contrib import admin
from .models import Products,Order
# Register your models here.

admin.site.site_header="E-commerce Site"
admin.site.site_title="ABC Shopping"
admin.site.index_title="Manage ABC Shopping"

class ProductAdmin(admin.ModelAdmin):
    def change_category_to_default(self,request,queryset):
        queryset.update(category="default")
        
    change_category_to_default.short_description="Default Category"
    list_display=  ('title','price','discount_price','category','description')
    search_fields = ('title','category',)
    actions = ('change_category_to_default',)
    fields = ('title','price','category','discount_price','description','image')
    list_editable = ('price','category','discount_price',)

class OrderAdmin(admin.ModelAdmin):
    list_display=  ('name','email','address','city','zipcode','total')
    search_fields = ('name','email','city','zipcode',)
    list_editable = ('email','zipcode',)

admin.site.register(Products,ProductAdmin)
admin.site.register(Order,OrderAdmin)