from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('<int:id>', views.view_student, name='view_student'),
  path('add/', views.add, name='add'),
  path('edit/<int:id>/', views.edit, name='edit'),
  path('delete/<int:id>/', views.delete, name='delete'), 
  path('register', views.register_request, name='register'), 
  path("login", views.login_request, name="login"),
  path("logout", views.logout_request, name= "logout"),
 ]