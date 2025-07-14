from django.db.models import Sum
from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets, generics
from rest_framework.decorators import api_view

from .models import Category, Candy, Customer, Order, OrderItem
from .serializers import CategorySerializer, CandySerializer, CustomerSerializer, OrderSerializer, OrderItemSerializer, \
    OrderDetailsSerializer


# Create your views here.
def contact(request, name):
    return HttpResponse(f"Bienvenido {name} a la clase de Django")


# Category
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryCreateView(generics.CreateAPIView, generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDeleteView(generics.DestroyAPIView, generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


# Candy
class CandyViewSet(viewsets.ModelViewSet):
    queryset = Candy.objects.all()
    serializer_class = CandySerializer


# Customer
class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


# Order
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


# OrderItem
class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer


@api_view(['GET'])
def get_order_items(request, order_id):
    try:
        order = Order.objects.get(id=order_id)
        customer_name = order.customer.first_name + " " + order.customer.last_name
        print(OrderItem.objects.all())
        order_details = OrderItem.objects.filter(order=order_id)
        total_cost = order_details.aggregate(Sum('price'))['price__sum']
        print('2', order_details)
        return JsonResponse(
            OrderDetailsSerializer({
                'order_details': order_details,
                'total_cost': total_cost,
                'customer_name': customer_name,
            }).data,
            safe=False,
            status=200,
        )
    except Exception as e:
        return JsonResponse({'message': str(e)}, status=400)
