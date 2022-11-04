from rest_framework.serializers import ModelSerializer

from .models import Event, Quote


class EventSerializer(ModelSerializer):
    class Meta:
        model = Event
        fields = ['scheduled_at','id','msg','image','holiday','added']





class QuoteSerializer(ModelSerializer):
    class Meta:
        model = Quote
        fields = ['id','author','quote']

