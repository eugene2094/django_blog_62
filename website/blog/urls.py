from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('post/<slug:post_slug>', views.get_post, name='post_detail'),
    path('contact/', views.contact, name='contact'),
    path('posts/create/', views.post_create, name='post_create'),
    path('posts/update/<int:id>', views.post_update, name='post_update'),
    path('register/', views.register, name='register'),
    # path('login/', views.login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
