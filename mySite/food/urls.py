from . import views
from django.urls import path

urlpatterns = [
    path('',views.index,name='index'),
    path('Item/',views.item,name='item')
]
