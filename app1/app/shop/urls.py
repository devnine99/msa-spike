from django.urls import path

from app.shop.views import ShopCreateView

urlpatterns = [
    path('', ShopCreateView.as_view()),
]
