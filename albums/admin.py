from django.contrib import admin
from .models import Album, Photo


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    # Fields shown in the album LIST page
    list_display = ('title', 'event_date', 'passkey', 'owner')

    # Fields shown when editing/creating an album — organized in sections
    fieldsets = (
        ('Album Info', {
            'fields': ('owner', 'title', 'event_date', 'description')
        }),
        ('🔒 Privacy', {
            'fields': ('passkey',),
            'description': 'Set a passkey to lock this album. Leave empty for public access.'
        }),
    )


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('album', 'uploaded_at')