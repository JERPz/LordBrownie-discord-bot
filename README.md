# 🐾 LordBrownie Discord Bot

A cute, cat-themed Discord bot built with Python!  
It can invite your friends to play games, play music from YouTube, and stay online forever on Replit (or your own server).


## ✨ Features

- 🎮 `!game <game> <time> @user ...`  
  Invite your friends to play a game with a styled embed.

- 🎵 `!play <YouTube URL>`  
  Join your voice channel and play audio from YouTube.

- ⏹️ `!stop`  
  Leave the voice channel and stop the music.

- 🌐 Replit keep-alive web server to prevent bot from sleeping.


## 🧰 Tech Stack

- Python `3.8+`
- [discord.py](https://pypi.org/project/discord.py/)
- [yt-dlp](https://github.com/yt-dlp/yt-dlp)
- [Flask](https://flask.palletsprojects.com/)
- `.env` for secure token storage

---
## 📁 Project Structure

```bash
📦 lordbrownie-discord-bot
├── main.py             # Main Discord bot logic
├── keep_alive.py       # Replit keep-alive web server
├── .env.example        # Example of environment variable file
├── requirements.txt    # Python dependencies
├── setup_run.sh        # Setup & run for Linux/macOS
├── setup_run.bat       # Setup & run for Windows
└── README.md

````

---

## 📦 Setup Instructions

### ✅ 1. Clone the Project

```bash
git clone https://github.com/JERPz/LordBrownie-discord-bot.git
cd LordBrownie-discord-bot
````

### ✅ 2. Create a `.env` File

Copy the example file:

```bash
cp .env.example .env
```

Then edit the `.env` file and replace with your actual token:

```env
BOT_TOKEN="your_real_discord_bot_token"
```

### ✅ 3. Install Dependencies

Using pip:

```bash
pip install -r requirements.txt
```

### ✅ 4. Run the Bot

Linux/macOS:

```bash
bash setup_run.sh
```

Windows:

```cmd
setup_run.bat
```

---

## 🧪 Testing

Try inviting your bot to your Discord server and type:

```text
!game valorant 8PM @friend
!play https://www.youtube.com/watch?v=abc123
!stop
```

---

## 🌐 Running on Replit?

* Make sure you add a **`.env` secret** with the key `BOT_TOKEN` and your bot token as the value.
* The bot uses `Flask` to keep the Replit project alive.

---

## ❤️ Credits

* Cat icon from [Flaticon](https://www.flaticon.com/free-icon/cat_1864514)
* Powered by Python, Discord API, and caffeine

````

---

## ✅ `.env.example`

```env
# Rename this file to `.env` and add your actual Discord bot token
BOT_TOKEN="your_discord_bot_token_here"
````
