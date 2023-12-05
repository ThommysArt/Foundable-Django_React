
from django.urls import path
from .views import *


urlpatterns = [
    path('cart-list', CartList.as_view()),
    path('cart-detail', CartDetail.as_view()),
    path('cart-item-list', CartItemList.as_view()),
    path('cart-item-detail', CartItemDetail.as_view()),
    path('purchase', PurchaseViewSet.as_view),
]
