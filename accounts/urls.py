from django.urls import path
from . import views
from .views import CustomSignupView

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('signup/', CustomSignupView.as_view(), name='account_signup'),
    path('signup_complete/', views.signup_complete, name='signup_complete'),
    path('', views.landing, name='landing'),  # Landing page URL
]






