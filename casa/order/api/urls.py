from django.urls import path
from .views import OrderDetailView, OrderListView
from order.views import *



urlpatterns = [
    path('order-list/', OrderListView.as_view(), name='order-list'),
    path('<int:pk>/order-detail/', OrderDetailView.as_view(), name='order-detail'),

]