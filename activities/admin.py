from django.contrib import admin

# Register your models here.

from .models import Schedule,Action

class ActionInline(admin.TabularInline):
    model = Action
    extra = 1


class ScheduleAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['description']}),
        ('Date information', {'fields': ['date_begin', 'date_end']}),
    ]

    inlines = [ActionInline]

    list_display = ('description', 'date_begin', 'date_end','is_open')

    list_filter = ['date_begin','date_end']


admin.site.register(Schedule,ScheduleAdmin)
admin.site.register(Action)