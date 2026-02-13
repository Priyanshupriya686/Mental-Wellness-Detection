import praw
import tweepy
import os

def get_reddit_client():
    """
    Get Reddit client with credentials from environment.
    """
    client_id = os.getenv('REDDIT_CLIENT_ID')
    client_secret = os.getenv('REDDIT_CLIENT_SECRET')
    user_agent = 'mental_wellness_app'

    if not client_id or not client_secret:
        raise ValueError("Reddit credentials not set in environment variables.")

    return praw.Reddit(
        client_id=client_id,
        client_secret=client_secret,
        user_agent=user_agent
    )

def get_twitter_client():
    """
    Get Twitter client with credentials from environment.
    """
    bearer_token = os.getenv('TWITTER_BEARER_TOKEN')

    if not bearer_token:
        raise ValueError("Twitter bearer token not set in environment variables.")

    return tweepy.Client(bearer_token=bearer_token)

def fetch_user_posts(platform, username, limit=10):
    """
    Fetch user posts from Reddit or X (Twitter).

    Args:
        platform (str): 'Reddit' or 'X'
        username (str): Username
        limit (int): Number of posts to fetch

    Returns:
        list: List of post texts
    """
    posts = []

    if platform == "Reddit":
        try:
            reddit = get_reddit_client()
            user = reddit.redditor(username)
            for post in user.submissions.new(limit=limit):
                posts.append(post.title + " " + post.selftext)

            if len(posts) == 0:
                posts.append("No posts found for this Reddit username.")
        except Exception as e:
            posts.append(f"Invalid Reddit username or error: {str(e)}")

    elif platform == "X":
        try:
            client_x = get_twitter_client()
            # Step 1: fetch user ID from username
            user_resp = client_x.get_user(username=username)
            if user_resp.data is None:
                posts.append("Invalid X username.")
            else:
                user_id = user_resp.data.id
                # Step 2: fetch tweets
                tweets_resp = client_x.get_users_tweets(id=user_id, max_results=limit)
                if tweets_resp.data:
                    for t in tweets_resp.data:
                        posts.append(t.text)
                else:
                    posts.append("No tweets found for this X username.")
        except Exception as e:
            posts.append(f"Error fetching X posts: {str(e)}")

    else:
        posts.append("Invalid platform selected.")

    return posts

def analyze_posts(posts):
    """
    Analyze posts for depression and wellness.

    Args:
        posts (list): List of post texts

    Returns:
        tuple: (depression_score, wellness_score, category)
    """
    # Check if posts are valid
    if not posts or all("No posts found" in p or "Invalid" in p or "Error" in p for p in posts):
        return None, None, "Invalid Username / No Posts Found"

    # Otherwise, do normal word-based analysis
    text = " ".join(posts).lower()
    depression_score = 0
    if "sad" in text or "depressed" in text:
        depression_score += 3
    if "happy" in text or "good" in text:
        depression_score -= 1

    # Clamp 0-5
    depression_score = max(0, min(5, depression_score))

    # Map to wellness score (0-100)
    wellness_score = 100 - depression_score * 10
    if wellness_score >= 75:
        category = "High"
    elif wellness_score >= 50:
        category = "Moderate"
    else:
        category = "Low"

    return depression_score, wellness_score, category