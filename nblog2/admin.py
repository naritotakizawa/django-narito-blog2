from django.contrib import admin
from django.db import models
from .models import *
from .widgets import FileUploadableTextArea
from adminsortable2 import admin as sortable_admin


class PageInline(sortable_admin.SortableInlineAdminMixin, admin.TabularInline):
    model = Page
    extra = 3
    formfield_overrides = {
        models.TextField: {'widget': FileUploadableTextArea},
    }


class NoteAdmin(admin.ModelAdmin):
    inlines = [PageInline]


admin.site.register(Note, NoteAdmin)
admin.site.register(Category)
