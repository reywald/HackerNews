from django.db import models
from django.urls import reverse
import uuid

# Create your models here.


class Base(models.Model):
    id = models.PositiveIntegerField(primary_key=True, editable=False)
    deleted = models.BooleanField(default=False)

    type = models.CharField(max_length=15, null=False)
    by = models.CharField(max_length=20, null=True, blank=True)
    time = models.PositiveIntegerField(null=True, blank=True)
    dead = models.BooleanField(default=False)
    kids = models.TextField(null=True)

    class Meta:
        abstract = True


class Comment(Base):

    parent = models.PositiveIntegerField(null=True, blank=True)
    text = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self) -> str:
        return self.text        # Truncate to 20 words

    def get_absolute_url(self):
        return reverse("comment_detail", kwargs={"pk": self.pk})


class Job(Base):

    score = models.PositiveIntegerField(null=True, blank=True)
    text = models.TextField(max_length=500, null=True, blank=True)
    url = models.URLField(null=True, blank=True)
    title = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse("job_detail", kwargs={"pk": self.pk})


class Poll(Base):

    parts = models.TextField(null=True)
    descendants = models.PositiveIntegerField(null=True, blank=True)
    score = models.PositiveIntegerField(null=True, blank=True)
    title = models.CharField(max_length=100, null=True, blank=True)
    text = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse("poll_detail", kwargs={"pk": self.pk})


class PollOption(Base):

    parent = models.PositiveIntegerField(null=True, blank=True)
    score = models.PositiveIntegerField(null=True, blank=True)
    text = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self) -> str:
        return self.parent

    def get_absolute_url(self):
        return reverse("poll_option_detail", kwargs={"pk": self.pk})


class Story(Base):

    descendants = models.PositiveIntegerField(null=True, blank=True)
    score = models.PositiveIntegerField(null=True, blank=True)
    title = models.CharField(max_length=100, null=True, blank=True)
    text = models.CharField(max_length=500, null=True, blank=True)
    url = models.URLField(null=True, blank=True)

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse("story_detail", kwargs={"pk": self.pk})
