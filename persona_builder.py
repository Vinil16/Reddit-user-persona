import os
import requests
from dotenv import load_dotenv
from pathlib import Path

load_dotenv(dotenv_path=Path('.') / '.env')

API_URL = "https://openrouter.ai/api/v1/chat/completions"
API_KEY = os.getenv("OPENROUTER_API_KEY")
MODEL = "deepseek/deepseek-r1-0528"

def generate_persona(username, texts):
    if not texts:
        return f"No Reddit activity found for u/{username}. Cannot generate persona."

    # Preformat Reddit data for clarity
    formatted_content = ""
    for i, entry in enumerate(texts[:20]):
        label = "POST" if "Post:" in entry else "COMMENT"
        parts = entry.split("\n")
        body = parts[0].replace("Comment: ", "").replace("Post: ", "")
        score_line = parts[1] if len(parts) > 1 else ""
        link = parts[-1] if len(parts) > 2 else ""
        formatted_content += f"[{label} #{i+1}] {body.strip()}\n{score_line}\n{link}\n\n"

    prompt = f"""
You are an expert UX researcher and content strategist.

Below is Reddit activity for user u/{username}. Each post or comment is numbered and includes its content and link.

Your task is to generate a clean and structured user persona in the following format. The style should be clear, creative, and resemble a UX persona created for product design or recruiting.

---
USER PERSONA: u/{username}

SUMMARY  
“A short, creative sentence capturing the user’s personality, values, or interests.”

BASIC INFO  
- Username: u/{username}  
- Likely Occupation: (infer from posts)  
- Location Clues: (any city or language mentioned)  
- Archetype: (e.g., The Analyst, The Creative, The Helper)

GOALS & NEEDS  
- Bullet point 1  
- Bullet point 2  

 PERSONALITY  
| Trait                 |     Tendency        |
|-----------------------|---------------------|
| Introvert ↔ Extrovert | Your judgment       |
| Sensing ↔ Intuition   | Your judgment       |
| Thinking ↔ Feeling    | Your judgment       |
| Judging ↔ Perceiving  | Your judgment       |

 BEHAVIOUR & HABITS  
- Example of behavior (mention subreddit or post link)  
-   

FRUSTRATIONS  
-  
-  

TOP INTERESTS  
Gaming / Simulation:  
Summary of strategy or game discussion. Cite subreddit or post.

AI Tools / Prompting:  
Summary of AI-related questions or thoughts.

Culture & Language:  
Any cultural/language comments or posts (e.g., Japanese, NYC).

Food & Lifestyle:  
Anything about food, cafes, or real-world hobbies.

Return the output exactly in that format. Avoid markdown.
Only use real, inferred data.
---

Reddit Activity:
{formatted_content}
"""

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://openrouter.ai",
        "X-Title": "Reddit Persona Builder"
    }

    payload = {
        "model": MODEL,
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7,
        "max_tokens": 2000
    }

    response = requests.post(API_URL, headers=headers, json=payload)

    if response.status_code == 200:
        result = response.json()["choices"][0]["message"]["content"]
        if result.strip() == "":
            return " Empty response from LLM. Try shortening content or rephrasing prompt."
        return result
    else:
        raise Exception(f"OpenRouter API Error {response.status_code}:\n{response.text}")
