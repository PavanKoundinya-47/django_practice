from django.urls import path
from .views import PostListView, \
    PostDetailView, \
    PostCreateView, \
    PostUpdateView, \
    PostDeleteView
from . import views


urlpatterns = [
    path("", PostListView.as_view(), name='test_db-home'),
    path("about/", views.about, name='test_db-about'),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("post/new/", PostCreateView.as_view(), name="post-create"),
    path("post/<int:pk>/update/", PostUpdateView.as_view(), name="post-update"),
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="post-delete"),
]

