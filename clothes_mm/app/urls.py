from django.urls import path
from . import views

app_name = 'app'
urlpatterns = [
    path('', views.index, name='index'),
    path('search', views.search, name='search'),
    path('clothes', views.show_clothes, name='clothes')
]
