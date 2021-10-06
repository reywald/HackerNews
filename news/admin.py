from django.contrib import admin
from .models import Comment, Job, Story, Poll, PollOption

# Register your models here.
admin.site.register(Comment)
admin.site.register(Job)
admin.site.register(Story)
admin.site.register(Poll)
admin.site.register(PollOption)