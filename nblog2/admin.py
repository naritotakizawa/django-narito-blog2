from django.contrib import admin
from .models import *
from adminsortable2 import admin as sortable_admin


class PageInline(sortable_admin.SortableInlineAdminMixin, admin.TabularInline):
    model = Page
    extra = 3


class NoteAdmin(admin.ModelAdmin):
    inlines = [PageInline]


admin.site.register(Note, NoteAdmin)
admin.site.register(Category)
