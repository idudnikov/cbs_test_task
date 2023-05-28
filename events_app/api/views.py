from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated

from events.models import Event, Organization

from .serializers import EventSerializer, OrganizationSerializer


class EventViewSet(viewsets.ModelViewSet):
    """
    Вьюсет модели мероприятия.
    """

    permission_classes = (IsAuthenticated,)
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    pagination_class = LimitOffsetPagination
    filter_backends = [OrderingFilter, SearchFilter, DjangoFilterBackend]
    filterset_fields = ['date', ]
    search_fields = ['^title', ]
    ordering_fields = ['date', ]


class OrganizationViewSet(viewsets.ModelViewSet):
    """
    Вьюсет модели организации.
    """

    permission_classes = (IsAuthenticated,)
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
