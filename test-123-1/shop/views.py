from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from shop.models import Item, Category, Tag

@api_view(["GET"])
def list_items(request):
    if request.method == "GET":
        items = Item.objects.values('id', 'name', 'price', 'category__name')
        return JsonResponse(list(items), safe=False)
    
def list_categories(request):
    if request.method == "GET":
        categories = Category.objects.values('id', 'name', 'description', 'images')
        return JsonResponse(list(categories), safe=False)
    
def list_tags(request):
    if request.method == "GET":
        tags = Tag.objects.values('id', 'name', 'items')
        return JsonResponse(list(tags), safe=False)