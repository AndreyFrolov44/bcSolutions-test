from django.contrib import admin
from .models import Block


@admin.register(Block)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('height', 'hash', 'date', 'miner', 'transaction',)
