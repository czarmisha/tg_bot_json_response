from django.contrib import admin

from .models import TgUser


class TgUserAdmin(admin.ModelAdmin):
    pass


admin.site.register(TgUser, TgUserAdmin)
