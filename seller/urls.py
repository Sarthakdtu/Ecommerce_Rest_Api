from django.urls import path
from seller.views import *

urlpatterns = [
    path('health-seller', api_health_check, name='seller_health'),
    path('seller-list', seller_list, name='seller_list'),
    path('seller-detail/<str:pk>', seller_detail, name='seller_detail'),
    path('seller-create', seller_create, name='seller_create'),
    path('seller-update/<str:pk>', seller_update, name='seller_update'),
    path('seller-delete/<str:pk>', seller_delete, name='seller_delete'),
]
