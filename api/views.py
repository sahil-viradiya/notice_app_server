from datetime import datetime, timedelta, time

from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .models import Event, Quote
from .serializers import EventSerializer, QuoteSerializer


@api_view(['GET'])
@permission_classes([AllowAny])
def load_current_event(request):
    today = datetime.now().date()
    tomorrow = today + timedelta(1)
    today_start = datetime.combine(today, time())
    today_end = datetime.combine(tomorrow, time())

    event = Event.objects.filter(scheduled_at__lte=today_end, scheduled_at__gte=today_start).first()
    data = EventSerializer(event).data
    return Response(data)


@api_view(['GET'])
@permission_classes([AllowAny])
def load_events(request):
    today = datetime.now().date()
    tomorrow = today + timedelta(1)
    today_start = datetime.combine(today, time())

    events = Event.objects.filter(scheduled_at__gte=today_start).order_by('scheduled_at')
    data = EventSerializer(events,many=True).data
    return Response(data)



@api_view(['GET'])
@permission_classes([AllowAny])
def load_quote(request):
    quote = Quote.objects.order_by("-id").first()
    data = QuoteSerializer(quote).data

    return Response(data)

