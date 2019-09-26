from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('deal', views.deals_list, name='deals_list')
]