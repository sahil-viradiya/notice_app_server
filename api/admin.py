from admin_interface.models import Theme
from django.contrib import admin
from django.contrib.auth.models import Group

from django.contrib.admin import register, ModelAdmin

from .models import Event, Quote
from .utils import send_notification


@register(Event)
class EventAdmin(ModelAdmin):
    list_display = ['scheduled_at','id','msg','image','holiday','added']

    def save_model(self, request, obj, form, change):
        super(EventAdmin,self).save_model(request, obj, form, change)
        send_notification("Holiday" if obj.holiday else "Event", obj.msg, obj.image)


@register(Quote)
class QuoteAdmin(ModelAdmin):
    list_display = ['author', 'id', 'quote']



admin.site.unregister(Group)

admin.site.unregister(Theme)
