
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('add',views.add,name='add'),
    path('substract',views.substract,name='substract'),
    path('divide',views.divide,name='divide'),
    path('multipy',views.multipy,name='multipy'),

]
