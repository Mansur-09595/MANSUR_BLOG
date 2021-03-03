from django.urls import path
from. import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('about/', views.About.as_view(), name='about'),
    path('signup/', views.SignUp.as_view(), name='signup'),
]