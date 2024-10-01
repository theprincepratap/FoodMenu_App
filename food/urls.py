from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:item_id>/',views.detail, name ="detail"),
    path('add/',views.add_item, name="add_item"),
    path('update/<int:item_id>/',views.update_item , name = "update_item"),
    path('delete/<int:item_id>/',views.delete_item, name = "delete_item")
]
