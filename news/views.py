from django.views.generic import ListView, DetailView
from .models import Comment, Job, Poll, PollOption, Story

from itertools import chain


class BaseListView(ListView):
    paginate_by = 10
    template_name = 'list.html'
    ordering = '-id'
    heading_type = ''

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['news_heading'] = self.heading_type
        context['news_types'] = {'all': "All News", 'job': "Jobs", 'poll': "Polls", 'story': "Stories"}

        return context


class NewsListView(BaseListView):
    heading_type = 'All News'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.all()
        context['jobs'] = Job.objects.all()
        context['polls'] = Poll.objects.all()
        context['polloptions'] = PollOption.objects.all()
        context['stories'] = Story.objects.all()

        return context

    def get_queryset(self):
        comments = Comment.objects.all()
        jobs = Job.objects.all()
        polls = Poll.objects.all()
        polloptions = PollOption.objects.all()
        stories = Story.objects.all()

        return sorted(chain(comments, jobs, polls, polloptions, stories), key=lambda item: item.id, reverse=True)


class CommentListView(BaseListView):
    model = Comment
    heading_type = 'Comments'


class CommentDetailView(DetailView):
    model = Comment
    template_name = 'detail.html'


class JobListView(BaseListView):
    model = Job
    heading_type = 'Jobs'


class JobDetailView(DetailView):
    template_name = 'detail.html'
    model = Job


class PollListView(BaseListView):
    model = Poll
    heading_type = 'Polls'


class PollDetailView(DetailView):
    template_name = 'detail.html'
    model = Poll


class StoryListView(BaseListView):
    model = Story
    heading_type = 'Stories'


class StoryDetailView(DetailView):
    template_name = 'detail.html'
    model = Story
