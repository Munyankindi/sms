from django.urls import path
from .import views

urlpatterns = [
    path('',views.stock ),
    path('contact/',views.contact),
    path('stock',views.stock,name='stock'),
    path('delete/<int:pk>',views.delete_stock_item_view,name='delete-stock'),
    path('update/<int:pk>',views.update_stock_item_view,name='update-stock'),
    path('contact/',views.contact)
]