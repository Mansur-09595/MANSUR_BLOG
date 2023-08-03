from django.urls import path
from. import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('signup/', views.SignUp.as_view(), name='signup'),
    #API URLS
    path('usersapi/', views.CustomUserCreateViewApi.as_view(), name='usersapi'),
    path('usersapi/<int:pk>/', views.CustomUserDetailViewApi.as_view(), name='userdetailapi'),
]