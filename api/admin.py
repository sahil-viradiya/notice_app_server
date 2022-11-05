import datetime

from admin_interface.models import Theme
from django.contrib import admin
from django.contrib.auth.models import Group

from django.contrib.admin import register, ModelAdmin
from django.utils.html import format_html

from .models import Event, Quote
from .utils import send_notification


@register(Event)
class EventAdmin(ModelAdmin):
    list_display = ['scheduled_At','msg','image','holiday','added']

    def save_model(self, request, obj, form, change):
        super(EventAdmin,self).save_model(request, obj, form, change)
        send_notification("Holiday" if obj.holiday else "Event", obj.msg, obj.image)

    def scheduled_At(self,obj):
        if obj.scheduled_at >= datetime.datetime.now().date():
            return obj.scheduled_at.strftime("%b. %d, %Y")
        else:
            return format_html(
                '<del style="color:gray">{}</del>',
                obj.scheduled_at.strftime("%b. %d, %Y")
            )




@register(Quote)
class QuoteAdmin(ModelAdmin):
    list_display = ['quote','author']

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False



admin.site.unregister(Group)

admin.site.unregister(Theme)
