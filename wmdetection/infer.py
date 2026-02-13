#!/usr/bin/env python3
"""
CLI for inference: analyze social media posts.
"""
import argparse
from wmdetection.app.social_analyzer import fetch_user_posts, analyze_posts

def main():
    parser = argparse.ArgumentParser(description="Analyze social media posts for wellness.")
    parser.add_argument("--platform", choices=["Reddit", "X"], required=True, help="Social media platform.")
    parser.add_argument("--username", required=True, help="Username to analyze.")
    parser.add_argument("--limit", type=int, default=10, help="Number of posts to fetch.")
    args = parser.parse_args()

    posts = fetch_user_posts(args.platform, args.username, args.limit)
    depression_score, wellness_score, category = analyze_posts(posts)

    print(f"Platform: {args.platform}")
    print(f"Username: {args.username}")
    if category == "Invalid Username / No Posts Found":
        print(f" {category}")
    else:
        print(f"Predicted Depression Level: {depression_score}")
        print(f"Wellness Score: {wellness_score}/100")
        print(f"Category: {category}")
        if category == "High":
            print(" You are doing great! Keep positive habits.")
        elif category == "Moderate":
            print(" Wellness moderate. Some improvement needed.")
        else:
            print(" Low wellness detected. Seek support if needed.")

if __name__ == "__main__":
    main()