from django.urls import path
from .views import CommentListView, CommentDetailView

urlpatterns = [
    path('news/<int:pk>', CommentDetailView, name='comment_detail'),
    path('', CommentListView.as_view(), name='comments'),
]
