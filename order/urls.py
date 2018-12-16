from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from order import views

urlpatterns = [
    path('orders/', views.OrderList.as_view(), name='orders-all'),
    path(
        'orders/<int:pk>/',
        views.OrderDetail.as_view(),
        name='order-delete-update-show'
    ),
]

urlpatterns = format_suffix_patterns(urlpatterns)
