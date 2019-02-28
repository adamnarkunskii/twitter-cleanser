#!/usr/bin/env python

import time
import twitter
from settings import (
    CONSUMER_KEY,
    CONSUMER_SECRET,
    ACCESS_TOKEN_KEY,
    ACCESS_TOKEN_SECRET,
    USER_NAME,
)


def init_api():
    return twitter.Api(
        sleep_on_rate_limit=True,
        consumer_key=CONSUMER_KEY,
        consumer_secret=CONSUMER_SECRET,
        access_token_key=ACCESS_TOKEN_KEY,
        access_token_secret=ACCESS_TOKEN_SECRET,
    )


def delete_favorites(api, statuses):
    for status in statuses:
        api.DestroyFavorite(status)
        print(status.user.name, status.created_at)


def delete_tweets(api):
    while True:
        api.DestroyStatus(api.GetUser(screen_name=USER_NAME).status.id)
        print(api.GetUser(screen_name=USER_NAME).statuses_count, "tweets remaining")


def main():
    api = init_api()
    while True:
        statuses = api.GetFavorites()
        if not statuses:
            break
        delete_favorites(api, statuses)
        delete_tweets(api)


if __name__ == "__main__":
    main()
