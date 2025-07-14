import os
import praw
from dotenv import load_dotenv

load_dotenv()

def fetch_user_data(username):
    reddit = praw.Reddit(
        client_id=os.getenv("REDDIT_CLIENT_ID"),
        client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
        user_agent="user-persona-scraper"
    )
    user = reddit.redditor(username)
    collected = []

    try:
        for comment in user.comments.new(limit=100):
            collected.append(f"Comment: {comment.body}\nScore: {comment.score}\nLink: https://www.reddit.com{comment.permalink}")
        for submission in user.submissions.new(limit=50):
            content = submission.selftext or submission.title
            collected.append(f"Post: {content}\nScore: {submission.score}\nLink: https://www.reddit.com{submission.permalink}")
    except Exception as e:
        print(f"Error fetching data: {e}")

    return collected
