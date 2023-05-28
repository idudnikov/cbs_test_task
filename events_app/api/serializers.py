from drf_extra_fields.fields import Base64ImageField
from rest_framework import serializers

from events.models import Event, Organization
from users.models import CustomUser as User


class UserSerializer(serializers.ModelSerializer):
    """
    Сериализатор модели пользователя.
    """

    class Meta:
        model = User
        fields = ('id', 'email')


class OrganizationSerializer(serializers.ModelSerializer):
    """
    Сериализатор модели организации.
    """

    users = UserSerializer(read_only=True, many=True, required=False)
    address = serializers.CharField(required=True, write_only=True)
    postcode = serializers.CharField(required=True, write_only=True)
    full_address = serializers.SerializerMethodField()

    class Meta:
        model = Organization
        fields = ('id', 'title', 'description', 'full_address', 'users', 'address', 'postcode')

    def get_full_address(self, obj):
        return f'{obj.postcode} {obj.address}'


class EventSerializer(serializers.ModelSerializer):
    """
    Сериализатор модели мероприятия.
    """

    organization = OrganizationSerializer(many=True, required=False)
    image = Base64ImageField(required=False)

    class Meta:
        model = Event
        fields = '__all__'

    def create(self, validated_data):
        organizations = Organization.objects.filter(id=self.initial_data.get('organization'))
        event = super().create(validated_data)
        event.organization.set(organizations)
        return event
