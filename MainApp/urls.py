from django.urls import path
from .views import LogRetrieveUpdateDestroyAPIView, LogListCreateAPIView
from . import views
from django.urls import path
from .views import (
    LogListCreateAPIView,
    LogRetrieveUpdateDestroyAPIView,
    BusinessListCreateAPIView,
    BusinessRetrieveUpdateDestroyAPIView,
)


urlpatterns = [
    path('logs/', LogListCreateAPIView.as_view(), name='log-list-create'),
    path('logs/<int:pk>/', LogRetrieveUpdateDestroyAPIView.as_view(), name='log-retrieve-update-destroy'),
    path('businesses/', BusinessListCreateAPIView.as_view(), name='business-list-create'),
    path('businesses/<int:pk>/', BusinessRetrieveUpdateDestroyAPIView.as_view(), name='business-retrieve-update-destroy'),
    path('combined-data/', LogListCreateAPIView.as_view(), name='combined-data-list-create'),
    path('', views.home , name='home'),
    path('01_per_reg/', views.per_reg , name='per_reg'),
    path('02_login/', views.login_view , name='login'),
    path('Per_home/', views.Per_home , name='Per_home'),
    path('business_home/', views.business_home , name='business_home'),
    path('003_business_reg/', views.Business_reg , name='Business_reg'),
    path('logout/', views.Loogout, name='logout'),
    path('changepass/', views.change_pass , name='cp'),
    path('per_profile/', views.per_profile, name='per_profile'),
    path('business_profile/', views.update_businessprofile, name='bp'),
]