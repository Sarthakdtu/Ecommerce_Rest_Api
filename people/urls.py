from django.urls import path
from people.views import *

urlpatterns = [
    path('health-customer', api_health_check, name='health_customer'),
    path('customer-list', customer_list, name='customer_list'),
    path('customer-detail/<str:pk>', customer_detail, name='customer_detail'),
    path('customer-create', customer_create, name='customer_create'),
    path('customer-update/<str:pk>', customer_update, name='customer_update'),
    path('customer-delete/<str:pk>', customer_delete, name='customer_delete'),
]
