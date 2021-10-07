from news.models import Comment, Job, Poll, PollOption, Story


class DBchecker():
    # Used by the HN Service to check if the tables are populated

    def check_dbs(self):
        # Check if data in tables by fetching first rows
        story_db = Story.objects.first()
        job_db = Job.objects.first()
        poll_db = Poll.objects.first()

        return poll_db is not None and job_db is not None and story_db is not None


class DBWriter():
    # Handles writing to the various tables

    def write_item_to_db(self, news_item: dict):
        # Check the type of item: job, story, comment, poll, pollopt
        # and delegate to the relevant function

        if news_item.type == 'job':
            self.__write_job_to_db(news_item)

        elif news_item.type == 'comment':
            self.__write_comments_to_db(news_item)

        elif news_item.type == 'poll':
            self.__write_poll_to_db(news_item)

        elif news_item.type == 'pollopt':
            self.__write_poll_option_to_db(news_item)

        elif news_item.type == 'story':
            self.__write_story_to_db(news_item)

    def __write_job_to_db(self, news_item: dict):
        job = Job(**news_item)
        job.save()

    def __write_comments_to_db(self, news_item: dict):
        comment = Comment(**news_item)
        comment.save()

    def __write_poll_to_db(self, news_item: dict):
        poll = Poll(**news_item)
        poll.save()

    def __write_poll_option_to_db(self, news_item: dict):
        poll_option = PollOption(**news_item)
        poll_option.save()

    def __write_story_to_db(self, news_item: dict):
        story = Story(**news_item)
        story.save()
