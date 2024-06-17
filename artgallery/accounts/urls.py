from django.urls import path
from . import views
from django.contrib.auth.views import PasswordChangeDoneView


app_name = 'accounts'

urlpatterns = [
    path('logout/', views.LogoutView.as_view(next_page='accounts:login'), name='logout'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('sign_up/', views.UserSignUpView.as_view(), name='sign_up'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('password_change/', views.CustomPasswordChangeView.as_view(), name='password_change'),
    path('password_change_done/', PasswordChangeDoneView.as_view(template_name='password_change_done.html'), name='password_change_done')
    
]

