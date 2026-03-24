from django.urls import path
from blog import views
urlpatterns = [
# path('', views.home, name='blog-home'),
path('about/', views.about, name='about-page'),
path('', views.PostListView.as_view(), name='blog-home'),
path('post/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
path('post/new/', views.PostCreateView.as_view(), name='post-create'),
]