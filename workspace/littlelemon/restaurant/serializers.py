from .models import MenuItem,Booking
from rest_framework import serializers

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['id','Title', 'Price', 'Inventory']

class BookingSerializer (serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'


