from django.core.management.base import BaseCommand
from shop.models import Category, Item, Tag
from django.db.models import Sum, Avg, Count, Min, Max
from django.contrib.contenttypes.models import ContentType
from django.apps import apps
from faker import Faker
from django.db import transaction
import time

faker = Faker()

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        category = Category(name='toys')
        category.save()