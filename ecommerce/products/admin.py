from django.contrib import admin
from .models import Kategoriya, Mahsulotlar, Mahsulot_rasm
from django.utils.html import format_html
from import_export.admin import ImportExportModelAdmin


class MahsulotRasmInline(admin.TabularInline):
    model = Mahsulot_rasm
    extra = 1
    max_num = 5

@admin.register(Mahsulotlar)
class MahsulotlarAdmin(ImportExportModelAdmin):
    inlines = [MahsulotRasmInline]
    list_display = ('name', 'category', 'price', 'oldprice', 'discount')
    list_filter = ('category',)
    search_fields = ('name', 'title')

@admin.register(Kategoriya)
class KategoriyaAdmin(admin.ModelAdmin):
    list_display = ('category_name',)
    search_fields = ('category_name',)
@admin.register(Mahsulot_rasm)
class MahsulotRasmAdmin(admin.ModelAdmin):
    list_display = ('product', 'image_thumbnail')
    list_filter = ('product__category',)
    search_fields = ('product__name', 'product__title')

    def image_thumbnail(self, obj):
        return format_html('<img src="{}" width="100" />', obj.image.url)

    image_thumbnail.short_description = 'Image'