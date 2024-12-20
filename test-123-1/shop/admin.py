from django.contrib import admin
from shop.models import Tag, Category, Item, Image
from shop.filters import PriceFilter

class ItemLine(admin.TabularInline):
    model = Item
    extra = 1
    
class TagInLine(admin.StackedInline):
    model = Item.tags.through
    extra = 1
    
class ItemInLine(admin.TabularInline):
    model = Tag.items.through
    extra = 1

class ImageInLine(admin.StackedInline):
    model = Image
    extra = 1
    fields = ('image',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    search_fields = ['name']
    ordering = ['name']
    inlines = [ItemLine, ImageInLine]
    
    def get_queryset(self, request):
        existing_queryset = super().get_queryset(request)
        return existing_queryset.prefetch_related('items')
    
    def first_five_items(self, obj):
        return ", ".join(item.name for item in obj.items.all()[:5])
    
class ItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'description']
    search_fields = ['name', 'description']
    ordering = ['-price']
    fields = ['name', 'price', 'category', 'description']
    autocomplete_fields = ['category']
    list_filter = [PriceFilter]
    inlines = [TagInLine, ImageInLine]
    
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    inlines = [ItemInLine]
    
admin.site.register(Tag,TagAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(Image)
