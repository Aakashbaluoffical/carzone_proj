from django.contrib import admin
from .models import car, banner
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


admin.site.register(car, car_admin, )


# banner poster are here
class banner_admin(admin.ModelAdmin):
    # banner image_1 is shorten and display jpg image
    def banner_1(self, object_1, ):
        return format_html(
            '<img src="{}" width = "60px" style="border-radius:2px"/>'.format(object_1.banner_image_1.url, ))

    # banner image_2 is shorten and display jpg image
    def banner_2(self, object_2, ):
        return format_html(
            '<img src="{}" width = "60px" style="border-radius:2px"/>'.format(object_2.banner_image_2.url, ))

    # banner image_3 is shorten and display jpg image
    def banner_3(self, object_3, ):
        return format_html(
            '<img src="{}" width = "60px" style="border-radius:2px"/>'.format(object_3.banner_image_3.url, ))

    list_display = ['id', 'banner_1', 'title_1', 'content_1', 'banner_2', 'title_2', 'content_2',
                    'banner_3', 'title_3', 'content_3', 'is_feature', ]
    list_display_links = ['id', 'title_1']
    list_editable = ['is_feature', ]


admin.site.register(banner, banner_admin, )
