# 🧠 Reddit User Persona Generator

This project is a creative, AI-powered script that generates **detailed user personas** by analyzing any public Reddit profile. It uses Reddit data (posts & comments) and a powerful LLM (DeepSeek via OpenRouter) to build clean, structured personas that highlight a user's personality traits, interests, habits, and motivations.

Ideal for **UX research**, **AI profiling**, or just exploring online behaviors in a meaningful way.

---

## ✨ What It Does

- 📥 Takes a Reddit user profile URL as input  
- 🔍 Scrapes their latest posts and comments using the Reddit API  
- 🤖 Sends the content to DeepSeek LLM via OpenRouter  
- 🧾 Outputs a clean, recruiter-style persona in `.txt` format (like you'd see in a UX research doc)  
- ✅ Includes motivations, frustrations, top interests, personality traits, and citations

---

## 🧱 Tech Stack

- **Python 3**
- [PRAW](https://praw.readthedocs.io/) – for accessing Reddit content
- [OpenRouter + DeepSeek](https://openrouter.ai) – for LLM-based persona generation
- `python-dotenv` – for managing API keys securely

---

## 📁 Project Structure

```
reddit-user-persona/
├── main.py               # CLI script – enter Reddit URL here
├── reddit_scraper.py     # Fetches posts/comments
├── persona_builder.py    # Generates structured persona using LLM
├── .env                  # Stores API keys (ignored in Git)
├── requirement.txt       # Python dependencies
├── README.md             # This file 🙂
└── <username>_persona.txt  # Output file with detailed persona
```

---

## ⚙️ How to Run It

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/reddit-user-persona.git
   cd reddit-user-persona
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirement.txt
   ```

3. **Create a `.env` file** in the project root with:
   ```env
   REDDIT_CLIENT_ID=your_reddit_client_id
   REDDIT_CLIENT_SECRET=your_reddit_client_secret
   OPENROUTER_API_KEY=your_openrouter_api_key
   ```

4. **Run the program**
   ```bash
   python main.py
   ```

5. **Enter a Reddit profile URL**
   Example:
   ```
   https://www.reddit.com/user/spez/
   ```

6. **Get the output**
   A text file like `spez_persona.txt` will be created with a structured persona based on that user's Reddit activity.

---

## 📌 Example Output

```
👤 USER PERSONA: u/spez

🧠 SUMMARY  
"A strategic leader balancing product innovation with community feedback..."

📍 BASIC INFO  
- Username: u/spez  
- Likely Occupation: Reddit CEO  
- ...
```

---

## 🧩 Future Ideas

- PDF export with branding
- Web UI version (Streamlit or Flask)
- Persona comparison tool
- Visualization of traits via charts

---

## 👨‍💻 Author

Developed by [Your Name].  
Made with 💬 + 🤖 for people who love internet psychology.

---
