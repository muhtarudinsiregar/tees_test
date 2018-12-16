from rest_framework import serializers, permissions

from order.models import Order


class OrderSerializer(serializers.ModelSerializer):
    name = serializers.ReadOnlyField(source='user.username')
    email = serializers.ReadOnlyField(source='user.email')
    permission_classes = (permissions.IsAuthenticated,)

    class Meta:
        model = Order
        fields = ('size', 'name', 'email')
