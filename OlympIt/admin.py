from django.contrib import admin
from .models import Lesson


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'icon_url', 'type')
    list_filter = ('type',)
    search_fields = ('id', 'name')
