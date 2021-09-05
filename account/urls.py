from account import views
from django.urls import path
urlpatterns = [
    path('reg',views.regi,name='reg'),
     path('log',views.login,name='log'),
    path('logout',views.logout,name='logout')
    ]