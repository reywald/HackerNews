# This script is used to run api calls to the Hacker News service
# It gets the latest news
import requests

# Scheduler's modules
from background_task import background
from datetime import datetime, timedelta
from time import timezone

from .db_services import DBchecker, DBWriter


baseUrl = "https://hacker-news.firebaseio.com/v0"
checker = DBchecker()
writer = DBWriter()


@background(schedule=5)
def get_latest_news():

    # Get most recent news if tables are populated
    # print(checker.check_dbs())
    # if checker.check_dbs():
    url = f"{baseUrl}/maxitem.json"
    response = requests.get(url)

    item = get_item_details(response.json())
    print(item, type(item))
    writer.write_item_to_db(item)

    # # Otherwise, get and process latest 100 records
    # else:

    #     # get the list of news items
    #     url = f"{baseUrl}/topstories.json"
    #     response = requests.get(url)
    #     news_items = response.json()

    #     selected_news_items = news_items[:100]
    #     for item in selected_news_items:
    #         item_details = get_item_details()
    #         writer.write_item_to_db(item_details)


def get_item_details(item):
  # get the details of the item
    url = f"{baseUrl}/item/{item}.json"
    response = requests.get(url)
    return response.json()


def schedule_task():
    today = datetime.now()

    # Calculate timezone
    hour_offset = timezone // (60 * 60)

    later = timedelta(hours=hour_offset, minutes=0, seconds=60)
    stop = today + later
    stop = datetime(stop.year, stop.month, stop.day, stop.hour,
                    stop.minute, stop.second, 0)

    return stop
