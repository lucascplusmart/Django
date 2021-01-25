from django.contrib import admin
from .models import Link
# Register your models here.
@admin.register(Link)
class LinkManager(admin.ModelAdmin):
    readonly_fields = ('created','changed')
    list_display = ('chave','created','changed')
