from django.contrib import admin
from shop.models import Tag, Category, Item, Image
from shop.filters import PriceFilter

# class ItemLine(admin.TabularInline):
#     model = Item
#     extra = 1
#     fields = ['name', 'price']
    
class ItemLine(admin.StackedInline):
    model = Item
    extra = 1
    fields = ['name', 'price']
    
class TagInLine(admin.TabularInline):
    model = Item.tags.through
    extra = 1
    
class ItemInLine(admin.TabularInline):
    model = Tag.items.through
    extra = 1

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'first_five_items']
    search_fields = ['id', 'name']
    ordering = ['id']
    inlines = [ItemLine]
    
    def get_queryset(self, request):
        existing_queryset = super().get_queryset(request)
        return existing_queryset.prefetch_related('items')
    
    def first_five_items(self, obj):
        return ", ".join(item.name for item in obj.items.all()[:5])
    
class ItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price']
    search_fields = ['name']
    ordering = ['price']
    fields = ['name', 'price', 'category', 'description']
    autocomplete_fields = ['category']
    list_filter = [PriceFilter]
    inlines = [TagInLine]
    
class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['id', 'name']
    ordering = ['id']
    inlines = [ItemInLine]
    
admin.site.register(Tag,TagAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(Image)
