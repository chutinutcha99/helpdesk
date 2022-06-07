from django.urls import path
from helpdeskusers import views
from django.contrib.auth import views as auth_views

app_name = 'helpdeskusers'

urlpatterns = [

    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='helpdeskusers/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='helpdeskusers/logout.html'), name='logout'),
    path('profile/', views.profile, name='profile'),
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='helpdeskusers/reset_password.html'), name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordChangeDoneView.as_view(template_name='helpdeskusers/reset_password_sent.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='helpdeskusers/reset_password_form.html'), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='helpdeskusers/reset_password_complete.html'), name='password_reset_complete'),
]