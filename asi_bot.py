# ============================================================
# PART 1 - IMPORTS
# ============================================================
import os
import time
import threading
from flask import Flask

from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes
)

# ============================================================
# PART 2 - ENV VARIABLES
# ============================================================
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

if not BOT_TOKEN:
    raise RuntimeError("BOT_TOKEN not set")

# ============================================================
# PART 3 - FLASK APP (FOR RENDER)
# ============================================================
app = Flask(__name__)

@app.route("/")
def home():
    return "ASI Telegram Bot is running ✅"

# ============================================================
# PART 4 - BOT LOGIC (SIMPLE & SAFE)
# ============================================================
def bot_status():
    return "🟢 ASI Bot is alive and running"

# ============================================================
# PART 5 - TELEGRAM COMMAND HANDLERS
# ============================================================
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 ASI Bot Started\n\n"
        "/status - bot status\n"
        "/ping - test command"
    )

async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(bot_status())

async def ping(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🏓 pong")

# ============================================================
# PART 6 - TELEGRAM APPLICATION SETUP
# ============================================================
application = Application.builder().token(BOT_TOKEN).build()

application.add_handler(CommandHandler("start", start))
application.add_handler(CommandHandler("status", status))
application.add_handler(CommandHandler("ping", ping))

# ============================================================
# PART 7 - BACKGROUND THREAD (KEEP ALIVE)
# ============================================================
def background_worker():
    while True:
        time.sleep(30)

threading.Thread(target=background_worker, daemon=True).start()

# ============================================================
# PART 8 - TELEGRAM BOT RUNNER
# ============================================================
def run_bot():
    print("🤖 Telegram bot polling started...")
    application.run_polling()

# ============================================================
# PART 9 - MAIN (FLASK + TELEGRAM)
# ============================================================
if __name__ == "__main__":
    # start telegram bot
    threading.Thread(target=run_bot, daemon=True).start()

    # run flask (Render requires this)
    port = int(os.environ.get("PORT", 10000))
    print(f"🌐 Flask running on port {port}")
    app.run(host="0.0.0.0", port=port)

import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is running"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
