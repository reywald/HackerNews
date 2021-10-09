from news.models import Comment, Job, Poll, PollOption, Story


class DBchecker():
    """
    Used by the HN Service to check if the tables are populated

    Methods
    -------
    check_dbs()
        Checks each model (Story, Job, Poll, Comment) for any recoreds.
    """

    def check_dbs(self):
        """ Check if data in tables by fetching first rows 
        
        Returns
        -------
        bool
            Whether any of the QuerySets are empty or populated
        """
        story_db = Story.objects.all().first()
        job_db = Job.objects.all().first()
        poll_db = Poll.objects.all().first()
        comment_db = Comment.objects.all().first()

        return poll_db is not None or job_db is not None or story_db is not None or comment_db is not None


class DBWriter():
    """
    Handles writing to the various tables
    ...

    Methods
    -------
    write_item_to_db(news_item: dict)
        Check the type of item: job, story, comment, poll, pollopt
    and delegate to the relevant function, which writes to the 
    proper database table

    write_xxx_to_db(news_item: dict)
        Commits the contents of the new_item dictionary object to
    its appropriate table. We have Job, Story, Comment, Poll & 
    Poll Option models. 
    Example: write_job_to_db(news_item) writes the news_item to
    the Job table
    """

    def write_item_to_db(self, news_item: dict):
        """ Check the type of item: job, story, comment, poll, pollopt
        and delegate to the relevant function, which writes to the 
        proper database table

        Parameters
        ----------
        news_item : dict
            The record to write to the database table
        """

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
