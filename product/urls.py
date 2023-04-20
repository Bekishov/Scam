from django.urls import path
from .views import ProductListAPIView, ProductCreateAPIView, ProductDetailAPIView, ProductUpdateAPIView, ProductDeleteAPIView


urlpatterns = [
    path('all', ProductListAPIView.as_view(), name='all-product'),
    path('create/', ProductCreateAPIView.as_view(), name='create-product'),
    path('<int:id>/update/', ProductUpdateAPIView.as_view(), name='update-product'),
    path('<int:id>/', ProductDetailAPIView.as_view(), name='retrieve-product'),
    path('<int:id>/delete', ProductDeleteAPIView.as_view(), name='delete-product'),
]