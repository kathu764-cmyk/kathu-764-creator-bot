import os
import threading

from flask import Flask
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    MessageHandler,
    ContextTypes,
    filters
)

TOKEN = os.environ["BOT_TOKEN"]

# =========================
# RENDER WEB SERVER
# =========================

web = Flask(__name__)


@web.route("/")
def home():
    return "KATHU 764 CREATOR BOT IS RUNNING 🔥"


def run_web():
    port = int(os.environ.get("PORT", 10000))
    web.run(
        host="0.0.0.0",
        port=port
    )


# =========================
# START
# =========================

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    keyboard = [
        [InlineKeyboardButton("🎨 Photo Edit", callback_data="photo")],
        [InlineKeyboardButton("🎬 Video Edit", callback_data="video")],
        [InlineKeyboardButton("🖼️ Poster Maker", callback_data="poster")],
        [InlineKeyboardButton("✍️ Caption + Hashtags", callback_data="caption")],
        [InlineKeyboardButton("💡 Content Ideas", callback_data="ideas")]
    ]

    await update.message.reply_text(
        "🔥 KATHU 764 CREATOR BOT\n\n"
        "Welcome! Choose what you need 👇",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


# =========================
# BUTTONS
# =========================

async def buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query
    await query.answer()

    context.user_data["mode"] = query.data

    messages = {
        "photo": "🎨 PHOTO EDIT\n\nSend your photo with your editing requirement.",
        "video": "🎬 VIDEO EDIT\n\nTell me your video editing idea.",
        "poster": "🖼️ POSTER MAKER\n\nTell me your poster topic.",
        "caption": "✍️ CAPTION + HASHTAGS\n\nSend your post or reel topic.",
        "ideas": "💡 CONTENT IDEAS\n\nTell me your content category."
    }

    await query.message.reply_text(messages[query.data])


# =========================
# PHOTO
# =========================

async def photo_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):

    requirement = update.message.caption

    if not requirement:
        requirement = "HD cinematic DSLR edit"

    prompt = f"""
🎨 KATHU 764 PHOTO EDIT PROMPT

Requirement:
{requirement}

Edit this uploaded photo professionally.

✨ HD + HDR quality
📷 Professional DSLR look
🎨 Cinematic colour grading
✨ Sharp and clean details
🌟 Natural skin tones
💡 Balanced exposure
🎬 Premium cinematic finish

Preserve the original face, identity,
clothes, jewellery, pose and important details.

Do not change the person's identity.
Do not over-edit the face.
"""

    await update.message.reply_text(prompt)


# =========================
# TEXT
# =========================

async def text_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = update.message.text
    mode = context.user_data.get("mode")

    if mode == "photo":

        reply = f"""
🎨 PHOTO EDIT PROMPT

Create a professional photo edit based on:

{text}

Use HD + HDR quality, cinematic colour grading,
natural skin tones, sharp details, DSLR look,
balanced lighting and premium finish.

Preserve the original face, identity,
clothes and important details.
"""

    elif mode == "video":

        reply = f"""
🎬 VIDEO EDIT PROMPT

Create a cinematic video edit based on:

{text}

Use smooth transitions, clear voice,
balanced background music, HD quality,
cinematic colour grading and engaging pacing.
"""

    elif mode == "poster":

        reply = f"""
🖼️ POSTER PROMPT

Create a premium Instagram poster based on:

{text}

Use cinematic lighting, clean composition,
bold readable typography, HD quality
and professional colour grading.
"""

    elif mode == "caption":

        reply = f"""
✍️ CAPTION + HASHTAGS

Topic:
{text}

🔥 Create a short catchy caption.

#Instagram #Reels #Creator #Kathu764
"""

    elif mode == "ideas":

        reply = f"""
💡 CONTENT IDEAS

Category:
{text}

1️⃣ Trending Reel
2️⃣ Before / After Edit
3️⃣ Quick Tutorial
4️⃣ Behind The Scenes
5️⃣ Creator Tips
6️⃣ Photo Editing Reel
7️⃣ Viral Hook Video
"""

    else:

        reply = "🔥 Use /start to open KATHU 764 CREATOR BOT."

    await update.message.reply_text(reply)


# =========================
# COMMANDS
# =========================

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(
        "🆘 KATHU 764 CREATOR BOT\n\n"
        "/start - Main Menu\n"
        "/help - Help"
    )


# =========================
# MAIN BOT
# =========================

def main():

    # Start Render web server
    threading.Thread(
        target=run_web,
        daemon=True
    ).start()

    # Telegram bot
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))

    app.add_handler(CallbackQueryHandler(buttons))

    app.add_handler(
        MessageHandler(
            filters.PHOTO,
            photo_handler
        )
    )

    app.add_handler(
        MessageHandler(
            filters.TEXT & ~filters.COMMAND,
            text_handler
        )
    )

    print("🔥 KATHU 764 CREATOR BOT STARTED")

    app.run_polling()


if __name__ == "__main__":
    main()
    
