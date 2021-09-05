from carts import views
from django.urls import path
urlpatterns = [
    path('details',views.cart,name='details'),
    path('add/<int:prdid>/',views.addcart,name='addcarts'),
    path('dec/<int:prdid>/',views.minus,name='minuss'),
    path('rm/<int:prdid>/',views.delete,name='removes')
    ]