from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('tourist-data/', views.get_tourist_data, name='tourist_data'),
    path('transport-data/', views.get_transport_data, name='transport_data'),
    path('traveldetail/<slug:place_id>/', views.traveldetail, name='traveldetail'),


]