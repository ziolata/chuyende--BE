from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Chapter)
class ChapterAdmin(admin.ModelAdmin):
    list_display = ('id','number','name','novel')
    list_filter = ['novel']
# admin.site.register(ChapterContent)
