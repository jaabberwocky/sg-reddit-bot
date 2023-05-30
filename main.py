import praw
from dotenv import load_dotenv
import os

load_dotenv()

REDDIT_CLIENT_ID = os.getenv("REDDIT_CLIENT_ID")
REDDIT_CLIENT_SECRET = os.getenv("REDDIT_CLIENT_SECRET")
REDDIT_USERNAME = os.getenv("REDDIT_USERNAME")
REDDIT_PASSWORD = os.getenv("REDDIT_PASSWORD")

reddit = praw.Reddit(
    client_id=REDDIT_CLIENT_ID,
    client_secret=REDDIT_CLIENT_SECRET,
    username=REDDIT_USERNAME,
    password=REDDIT_PASSWORD,
    user_agent="reddit bot")


def is_alphabetical_order(word):
    return word == "".join(sorted(word))


def has_69_char(body: str) -> bool:
    return len(body) == 69


if __name__ == "__main__":
    for comment in reddit.subreddit("asksingapore").stream.comments():
        print(
            f"New comment by {comment.author} in {comment.parent_id}: {comment.body}")

        if has_69_char(comment.body):
            print("***Comment has 69 characters!***")
            print(
                f"{comment.id} by {comment.author} in {comment.parent_id}: {comment.body}")
