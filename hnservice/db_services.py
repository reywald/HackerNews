from news.models import Comment, Job, Poll, PollOption, Story


class DBchecker():
    # Used by the HN Service to check if the tables are populated

    def check_dbs(self):
        # Check if data in tables by fetching first rows
        story_db = Story.objects.first()
        job_db = Job.objects.first()
        poll_db = Poll.objects.first()
        comment_db = Comment.objects.first()

        return poll_db is not None or job_db is not None or story_db is not None or comment_db is not None


class DBWriter():
    # Handles writing to the various tables

    def write_item_to_db(self, news_item: dict):
        # Check the type of item: job, story, comment, poll, pollopt
        # and delegate to the relevant function

        if news_item["type"] == 'job':
            self.__write_job_to_db(news_item)

        elif news_item["type"] == 'comment':
            self.__write_comments_to_db(news_item)

        elif news_item["type"] == 'poll':
            self.__write_poll_to_db(news_item)

        elif news_item["type"] == 'pollopt':
            self.__write_poll_option_to_db(news_item)

        elif news_item["type"] == 'story':
            self.__write_story_to_db(news_item)

    def __write_job_to_db(self, news_item: dict):
        Job.objects.get_or_create(**news_item)

    def __write_comments_to_db(self, news_item: dict):
        Comment.objects.get_or_create(**news_item)

    def __write_poll_to_db(self, news_item: dict):
        Poll.objects.get_or_create(**news_item)

    def __write_poll_option_to_db(self, news_item: dict):
        PollOption.objects.get_or_create(**news_item)

    def __write_story_to_db(self, news_item: dict):
        Story.objects.get_or_create(**news_item)
