from django.urls import path
from . import views


app_name = 'accounts'

urlpatterns = [
    path('logout/', views.LogoutView.as_view(next_page='accounts:login'), name='logout'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('sign_up/', views.UserSignUpView.as_view(), name='sign_up')
    
]

