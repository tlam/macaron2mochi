from django.contrib import admin

from activities.models import Activity


class ActivityAdmin(admin.ModelAdmin):
    list_display = ('name', 'category',)
    search_fields = ['name']

admin.site.register(Activity, ActivityAdmin)
