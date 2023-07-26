from django.urls import path
from . import views

app_name = 'map'


urlpatterns = [
    path('accounts/', views.AccountsAPIMixins.as_view(), name='accounts'),
    path('account/<str:userid>/', views.AccountAPIMixins.as_view(), name='account'),
    
    path('wps/', views.WPsAPIMixins.as_view(), name='wps'),
    path('wps/<int:waterplaysubid>/', views.WPsTypeAPIMixins.as_view(), name='wpstype'),
    
    path('wp/<int:waterplayid>/', views.WPAPIMixins.as_view(), name='wp'),
]
