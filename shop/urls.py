from django.urls import path
from shop.views import ProductView_get


urlpatterns = [
    path("<int:id>", ProductView_get.as_view()),
]
