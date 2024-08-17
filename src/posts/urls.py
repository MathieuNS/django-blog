from django.urls import path

from posts.views import BlogHome, BlogPostCreate, BlogPostUpdate, BlogPostView, BlogPostDelete

app_name = 'posts'

urlpatterns = [
    path('', BlogHome.as_view(), name="home"),
    path('create', BlogPostCreate.as_view(), name="create"),
    path('update/<str:slug>/', BlogPostUpdate.as_view(), name="update"),
    path('delete/<str:slug>/', BlogPostDelete.as_view(), name="delete"),
    path('<str:slug>/', BlogPostView.as_view(), name="article"),
]