from rest_framework import viewsets, permissions

from news import models
from .serializers import (
    CommentSerializer, JobSerializer, PollSerializer,
    PollOptionSerializer, StorySerializer
)

from drf_multiple_model.viewsets import ObjectMultipleModelAPIViewSet
from drf_multiple_model.pagination import MultipleModelLimitOffsetPagination


class LimitPagination(MultipleModelLimitOffsetPagination):
    default_limit = 10


class HomeViewSet(ObjectMultipleModelAPIViewSet):
    pagination_class = LimitPagination
    querylist = [
        {'queryset': models.Story.objects.order_by(
            '-id'), 'serializer_class': StorySerializer},
        {'queryset': models.Comment.objects.order_by(
            '-id'), 'serializer_class': CommentSerializer},
        {'queryset': models.Job.objects.order_by(
            '-id'), 'serializer_class': JobSerializer},
        {'queryset': models.Poll.objects.order_by(
            '-id'), 'serializer_class': PollSerializer},
        {'queryset': models.PollOption.objects.order_by(
            '-id'), 'serializer_class': PollOptionSerializer},
    ]


class CommentViewSet(viewsets.ModelViewSet):
    queryset = models.Comment.objects.all()
    serializer_class = CommentSerializer


class JobViewSet(viewsets.ModelViewSet):
    queryset = models.Job.objects.all()
    serializer_class = JobSerializer


class PollViewSet(viewsets.ModelViewSet):
    queryset = models.Poll.objects.all()
    serializer_class = PollSerializer


class PollOptionViewSet(viewsets.ModelViewSet):
    queryset = models.PollOption.objects.all()
    serializer_class = PollOptionSerializer


class StoryViewSet(viewsets.ModelViewSet):
    queryset = models.Story.objects.all()
    serializer_class = StorySerializer
