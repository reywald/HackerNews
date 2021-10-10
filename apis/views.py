from rest_framework import viewsets, permissions

from news import models
from .serializers import (
    CommentSerializer, JobSerializer, PollSerializer,
    PollOptionSerializer, StorySerializer
)


# class ListAll(generics.ListAPIView):

#     def get(self, request, *args, **kwargs):
#         comment_serializer = CommentSerializer(models.Comment.objects.all())
# job_serializer = JobSerializer(models.Job.objects.all())
# poll_serializer = PollSerializer(models.Poll.objects.all())
# poll_option_serializer = PollOptionSerializer(models.PollOption.objects.all())
# story_serializer = StorySerializer(models.Story.objects.all())

# return Response({
#     'comments': comment_serializer.data,
# })
# 'jobs': job_serializer.data,
# 'polls': poll_serializer.data,
# 'poll_options': poll_option_serializer.data,
# 'stories': story_serializer.data,


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
