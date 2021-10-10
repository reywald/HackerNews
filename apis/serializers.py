from rest_framework import serializers
from news import models

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'by', 'time', 'text')
        model = models.Comment

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'by', 'time', 'title', 'text', 'url')
        model = models.Job

class PollSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'by', 'time', 'title', 'text', 'score')
        model = models.Poll

class PollOptionSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'by', 'time', 'text', 'score')
        model = models.PollOption
        
class StorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'by', 'time', 'title', 'url')
        model = models.Story