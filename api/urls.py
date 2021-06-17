from django.urls import path

from . import views

urlpatterns = [
    path('', views.test, name="test"),

    path('category/', views.CategoryListView.as_view(), name="category"),
    path('category/<int:pk>', views.CategoryDetailView.as_view(), name="category_detail"),

    path('book/', views.BookListView.as_view(), name="book"),
    path('book/<int:pk>', views.BookDetailView.as_view(), name="book_detail"),

    path('product/', views.ProductListView.as_view(), name="product"),
    path('product/<int:pk>', views.ProductDetailView.as_view(), name="product_detail"),
]
