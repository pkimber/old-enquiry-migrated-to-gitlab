from django.contrib import admin

from .models import Notify


class NotifyAdmin(admin.ModelAdmin):
    pass

admin.site.register(Notify, NotifyAdmin)
