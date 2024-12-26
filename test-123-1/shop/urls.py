from django.urls import path 
from shop.views import list_items, list_categories, list_tags

urlpatterns = [
    path('items/', list_items, name='list Items'),
    path('categories/', list_categories, name='list categories'),
    path('tags/', list_tags, name='list tags')
]