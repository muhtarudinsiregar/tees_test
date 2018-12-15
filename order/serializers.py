from rest_framework import serializers

from order.models import Order


class OrderSerializer(serializers.ModelSerializer):
    email = serializers.ReadOnlyField(source='user_id.email')
    name = serializers.ReadOnlyField(source='user_id.first_name')

    class Meta:
        model = Order
        fields = ('size', 'id')
