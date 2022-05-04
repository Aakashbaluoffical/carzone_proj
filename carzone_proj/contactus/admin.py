from django.contrib import admin
from .models import contactus


# Register your models here.


class contactusAdmin(admin.ModelAdmin):
    list_display = ['id', 'fullname', 'email', 'subject', 'number', 'subject', ]
    list_display_links = ['id', 'fullname', ]


admin.site.register(contactus, contactusAdmin)
