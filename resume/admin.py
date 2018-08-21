from django.contrib import admin

from .models import Artist, Language


class LanguageAdmin(admin.ModelAdmin):
    readonly_fields = ('name',)

    def get_read_only_fields(self, request, obj=None):
        if obj:
            return ['name']
        return []


class LanguageInline(admin.TabularInline):
    model = Language.artist.through
    extra = 0


class ArtistAdmin(admin.ModelAdmin):
    date_hierarchy = 'date_created'
    readonly_fields = ('email',)
    inlines = (LanguageInline,)

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ['email']
        return []


admin.site.register(Artist, ArtistAdmin)
admin.site.register(Language, LanguageAdmin)
