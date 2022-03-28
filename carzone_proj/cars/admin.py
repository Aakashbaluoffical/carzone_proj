from django.contrib import admin
from .models import car
from django.utils.html import format_html


# Register your models here.


class car_admin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width = "40px" style="border-radius:2px"/>'.format(object.car_photo.url))

    list_display = ['id', 'thumbnail', 'car_title', 'year', 'state', 'colour', 'no_of_owners', 'price', 'is_feature',
                    'created_date', ]
    list_display_links = ['thumbnail', 'car_title', ]
    list_editable = ['is_feature', ]

    search_fields = ['id', 'car_title', 'city', 'state', 'year', 'colour', 'no_of_owners', 'price', ]
    list_filter = ['city', 'model', 'body_style', 'fuel_type', ]

admin.site.register(car, car_admin)
