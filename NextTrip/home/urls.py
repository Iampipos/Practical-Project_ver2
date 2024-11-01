from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('tourist-data/', views.get_tourist_data, name='tourist_data'),
    path('transport-data/', views.get_transport_data, name='transport_data'),
    path('traveldetail/<slug:place_id>/', views.traveldetail, name='traveldetail'),
    path('register/', views.register, name='register'),
    path('detail_data/', views.get_detail_data, name='detail_data'),
    path('check-email/', views.check_email_exists, name='check_email_exists'),


]