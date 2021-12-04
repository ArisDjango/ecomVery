from django.urls import path

from . import views

app_name = 'basket'

urlpatterns = [
    path('', views.basket_summary, name='basket_summary'),
    # path('add/',views.basket_add, name='add_basket'),
    # path('delete/', views.basket_delete, name='delete_basket'),
    # path('update/', views.basket_update, name='update_basket'),
    ]
