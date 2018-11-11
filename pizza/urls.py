from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('', TemplateView.as_view(template_name="home.html"), name='home'),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('loveit/<int:pk>/', views.LoveItView, name="love-it"),
    path('users/', views.ListUsersView.as_view(), name="all-users")
]
