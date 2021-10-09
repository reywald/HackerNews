from django.urls import path
from .views import (
    CommentListView, CommentDetailView, JobListView, JobDetailView,
    NewsListView, PollDetailView, PollListView, StoryDetailView, StoryListView
)

urlpatterns = [
    path('comment/<int:pk>', CommentDetailView.as_view(), name='comment_detail'),
    path('job/<int:pk>', JobDetailView.as_view(), name='job_detail'),
    path('poll/<int:pk>', PollDetailView.as_view(), name='poll_detail'),
    path('story/<int:pk>', StoryDetailView.as_view(), name='story_detail'),

    path('stories/', StoryListView.as_view(), name='stories'),
    path('jobs/', JobListView.as_view(), name='jobs'),
    path('polls/', PollListView.as_view(), name='polls'),
    path('', NewsListView.as_view(), name='all_news'),
]
