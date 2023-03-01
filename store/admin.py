from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['image_preview','name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
    readonly_fields = ["image_preview"]

    def image_preview(self, obj):
        print(obj.image.url)
        return mark_safe(f'<img src="{obj.image.url}" width="85px">')






@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'producer', 'designation', 'quantity', 'image_preview', 'price',
                    'in_stock', ]
    list_filter = ['in_stock', 'is_active', 'title']
    search_fields = ('designation', 'name')
    list_editable = ['price', 'in_stock', 'quantity', ]
    prepopulated_fields = {'slug': ('title',)}

    readonly_fields = ["image_preview"]

    def image_preview(self, obj):
        print(obj.image.url)
        return mark_safe(f'<img src="{obj.image.url}" width="80px">')
