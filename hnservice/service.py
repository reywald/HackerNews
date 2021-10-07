# This script is used to run api calls to the Hacker News service
# It gets the latest news
import requests
from news.models import Comment


def get_latest_news():
    # get the list of news items
    url = "https://hacker-news.firebaseio.com/v0/topstories.json"
    response = requests.get(url)
    news_items = response.json()


def get_item_details(item):
    # get the details of the item
    url = f"https://hacker-news.firebaseio.com/v0/item/{item}.json"
    response = requests.get(url)
    news_item = response.json()


def write_item_to_db(news_item: dict):
    # Check the type of item: job, story, comment, poll, pollopt