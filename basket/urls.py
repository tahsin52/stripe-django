from django.urls import path
from . import views

app_name = 'basket'

urlpatterns = [
    path('', views.basket_summary, name='basket_summary'),
    path('basket/add/', views.basket_add, name='basket_add'),
    path('basket/delete/', views.basket_delete, name='basket_delete'),
    path('basket/update/', views.basket_update, name='basket_update'),
]
