from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'), # pk is primary key, post-detail is the default view name
    path('post/new/', PostCreateView.as_view(), name='post-create'), # default view is post_form. Same as update view
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'), # pk is primary key, post-update uses post_form.html
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'), # pk is primary key, post-delete uses post_confirm_delete.html
    path('about/', views.about, name='blog-about'),
]
