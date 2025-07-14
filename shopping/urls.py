from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'category', views.CategoryViewSet)
router.register(r'candy', views.CandyViewSet)
router.register(r'customer', views.CustomerViewSet)
router.register(r'order', views.OrderViewSet)
router.register(r'orderItem', views.OrderItemViewSet)

urlpatterns = [
    path('contact/<str:name>/', views.contact, name='contact'),
    path('category/create/', views.CategoryCreateView.as_view(), name='category-create'),
    path('category/delete/<int:pk>/', views.CategoryDeleteView.as_view(), name='category-delete'),
    path('order/orderDetails/<int:order_id>/', views.get_order_items, name='order-details'),
    path('', include(router.urls)),
]