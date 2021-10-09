from django.urls import path
from .views import CommentListView, CommentDetailView, JobListView, PollListView,  StoryListView

urlpatterns = [
    path('comment/<int:pk>', CommentDetailView.as_view(), name='comment_detail'),
    path('stories/', StoryListView.as_view(), name='stories'),
    path('jobs/', JobListView.as_view(), name='jobs'),
    path('polls/', PollListView.as_view(), name='polls'),
    path('', CommentListView.as_view(), name='comments'),
]
