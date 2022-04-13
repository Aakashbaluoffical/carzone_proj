from django.contrib import admin
from .models import Contact


# Register your models here.
class contactAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'car_id', 'customer_need', 'car_title', 'user_id', 'city', 'state',
                    'email', 'message', 'phone', 'created_date', ]
    list_display_links = ['id', 'first_name', ]
    search_fields = ['id', 'first_name', 'last_name', 'customer_need', 'city', 'state', 'car_title', ]
    list_filter = ['car_title', 'city', 'state', 'customer_need', ]
    list_per_page = 25


admin.site.register(Contact, contactAdmin)
