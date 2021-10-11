from rest_framework import urlpatterns
from rest_framework.routers import SimpleRouter

from .views import (
    CommentViewSet,
    JobViewSet,
    PollOptionViewSet,
    PollViewSet,
    StoryViewSet,
    HomeViewSet
)

router = SimpleRouter()
router.register('comments', CommentViewSet, basename='comments_api')
router.register('jobs', JobViewSet, basename='jobs_api')
router.register('polls', PollViewSet, basename='polls_api')
router.register('polloptions', PollOptionViewSet, basename='poll_options_api')
router.register('stories', StoryViewSet, basename='stories_api')
router.register('', HomeViewSet, basename='all_api')

urlpatterns = router.urls
