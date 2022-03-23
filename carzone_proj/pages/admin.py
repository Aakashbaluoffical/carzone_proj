from django.contrib import admin
from .models import team
from django.utils.html import format_html


# Register your models here.
class team_admin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width = "40px" style="border-radius:10px"/>'.format(object.photos.url))
    list_display = ['id', 'thumbnail', 'first_name', 'last_name', 'position', 'created_date']
    list_display_links = ('thumbnail', 'first_name',)
    search_fields = ['id', 'first_name', 'position', ]
    list_filter = ['position', 'created_date']


admin.site.register(team, team_admin)
