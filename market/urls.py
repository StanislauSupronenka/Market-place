from django.urls import path
from . import views

urlpatterns = [
    path('home', views.main, name='main'),
    path('deal', views.deals_list, name='deals_list'),
    path('chart', views.get_stats, name='charts'),
    path('', views.sign_in, name='charts'),
    path('table', views.table, name='charts'),

]