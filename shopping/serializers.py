from rest_framework import serializers

from .models import Category, Candy, Customer, Order, OrderItem


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class CandySerializer(serializers.ModelSerializer):
    class Meta:
        model = Candy
        fields = '__all__'


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'


class OrderDetailsSerializer(serializers.Serializer):
    order_details = OrderItemSerializer(many=True)
    total_cost = serializers.IntegerField()
    customer_name = serializers.CharField()
