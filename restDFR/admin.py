from django.contrib import admin
from restDFR.models import Game, Category


class GameAdmin(admin.ModelAdmin):
    list_display = "id", "title", "time_create", "time_update", "cat"
    list_display_links = "id", "title"
    search_fields = "title".split()


admin.site.register(Game, GameAdmin)
admin.site.register(Category)
