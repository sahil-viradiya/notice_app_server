
from django.urls import path

from . import views

urlpatterns = [
    path('current_event/', views.load_current_event),
    path('load_events/', views.load_events),
    path('quote/', views.load_quote),
]