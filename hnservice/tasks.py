# This script is used to run api calls to the Hacker News service
# It gets the latest news
import requests

# Scheduler's modules
from background_task import background, tasks
from background_task.models import Task
from datetime import datetime, timedelta
import pytz

from .db_services import DBchecker, DBWriter


baseUrl = "https://hacker-news.firebaseio.com/v0"
checker = DBchecker()
writer = DBWriter()


@background(schedule=60)
def get_latest_news():

    # Get most recent news if tables are populated
    if checker.check_dbs():
        url = f"{baseUrl}/maxitem.json"
        response = requests.get(url)

        item = get_item_details(response.json())
        # print(item, type(item))
        writer.write_item_to_db(item)

    # Otherwise, get and process latest 100 records
    else:

        # get the list of news items
        url = f"{baseUrl}/topstories.json"
        response = requests.get(url)
        news_items = response.json()

        selected_news_items = news_items[:100]
        for item in selected_news_items:
            item_details = get_item_details(item)
            writer.write_item_to_db(item_details)


def get_item_details(item):
  # get the details of the item
    url = f"{baseUrl}/item/{item}.json"
    response = requests.get(url)
    return response.json()


def stop_task():
    pass


def start_task():
    tasks = Task.objects.filter(verbose_name="Get Latest News")
    if len(tasks) == 0:

        # Schedule to stop after 1 hour
        stop = datetime.utcnow().replace(tzinfo=pytz.utc) + \
            timedelta(hours=1, minutes=0, seconds=0)

        # No task running with this name, call background tasks every 5 minutes
        get_latest_news(schedule=timedelta(seconds=60), repeat=300,
                        repeat_until=stop, verbose_name="Get Latest News")
