import os
from reddit_scraper import fetch_user_data
from persona_builder import generate_persona

def main():
    reddit_url = input("Enter Reddit user URL: ").strip()

    if not reddit_url.startswith("https://www.reddit.com/user/"):
        print(" Invalid Reddit user URL format.")
        return

    username = reddit_url.rstrip("/").split("/")[-1]
    print(f"Extracting data for user: {username}...")

    posts = fetch_user_data(username)

    if not posts:
        print(f"No posts/comments found for u/{username}")
        return

    print("Generating persona using DeepSeek via OpenRouter...")
    persona = generate_persona(username, posts)

    filename = f"{username}_persona.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(persona)

    print(f"Persona saved to: {filename}")

if __name__ == "__main__":
    main()
