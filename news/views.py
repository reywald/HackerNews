from django.views.generic import ListView, DetailView
from .models import Comment, Job, Poll, PollOption, Story


class NewsListView(ListView):
    template_name = 'list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.all()
        context['jobs'] = Job.objects.all()
        context['polls'] = Poll.objects.all()
        context['polloptions'] = PollOption.objects.all()
        context['stories'] = Story.objects.all()

        return context


class CommentListView(ListView):
    model = Comment
    template_name = 'list.html'
    context_object_name = 'comments'


class CommentDetailView(DetailView):
    model = Comment
    template_name = 'detail.html'


class JobDetailView(DetailView):
    template_name = 'detail.html'
    model = Job
