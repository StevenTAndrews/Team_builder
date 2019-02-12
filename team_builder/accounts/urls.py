from django.urls import path

from . import views

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('signin/', views.LoginView.as_view(), name='signin'),
    path('signout/', views.LogoutView.as_view(), name='signout'),
    path('<pk>/', views.profile_detail, name='profile'),
    path('<pk>/edit', views.profile_edit, name='edit')
]