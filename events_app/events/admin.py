from django.contrib import admin

from .models import Event, Organization


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    """
    ПОдключение модели мероприятия к админ-панели.
    """

    list_display = ('id', 'title')
    list_filter = ('title', 'organization', 'date')
    readonly_fields = ('thumbnail_preview',)
    search_fields = ['title']

    def thumbnail_preview(self, obj):
        return obj.thumbnail_preview

    thumbnail_preview.short_description = 'Thumbnail Preview'
    thumbnail_preview.allow_tags = True


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    """
    ПОдключение модели организации к админ-панели.
    """

    list_display = ('id', 'title')
    list_filter = ('title', 'address', 'postcode')
    search_fields = ['title']
