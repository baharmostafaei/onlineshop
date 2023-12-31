from django.urls import path
from . import views
urlpatterns = [
    path('', views.home_view, name='home'),
    path('products/', views.ProductListView.as_view(), name= 'product_list'), 
    path('products/<int:pk>/', views.ProductDetailView.as_view(), name='product_detail'),
]
