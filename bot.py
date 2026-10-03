import os

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
# START MENU
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
# PHOTO COMMAND
# =========================

async def photo_command(update: Update, context: ContextTypes.DEFAULT_TYPE):

    context.user_data["mode"] = "photo"

    await update.message.reply_text(
        "🎨 PHOTO EDIT MODE\n\n"
        "Send your photo with a short requirement.\n\n"
        "Example:\n"
        "HD cinematic DSLR edit"
    )


# =========================
# VIDEO COMMAND
# =========================

async def video_command(update: Update, context: ContextTypes.DEFAULT_TYPE):

    context.user_data["mode"] = "video"

    await update.message.reply_text(
        "🎬 VIDEO EDIT MODE\n\n"
        "Tell me your video editing idea."
    )


# =========================
# POSTER COMMAND
# =========================

async def poster_command(update: Update, context: ContextTypes.DEFAULT_TYPE):

    context.user_data["mode"] = "poster"

    await update.message.reply_text(
        "🖼️ POSTER MODE\n\n"
        "Tell me your poster topic and size."
    )


# =========================
# CAPTION COMMAND
# =========================

async def caption_command(update: Update, context: ContextTypes.DEFAULT_TYPE):

    context.user_data["mode"] = "caption"

    await update.message.reply_text(
        "✍️ CAPTION MODE\n\n"
        "Send your post or reel topic."
    )


# =========================
# IDEAS COMMAND
# =========================

async def ideas_command(update: Update, context: ContextTypes.DEFAULT_TYPE):

    context.user_data["mode"] = "ideas"

    await update.message.reply_text(
        "💡 CONTENT IDEAS MODE\n\n"
        "Tell me your content category."
    )


# =========================
# BUTTONS
# =========================

async def buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query

    await query.answer()

    context.user_data["mode"] = query.data

    messages = {

        "photo":
        "🎨 PHOTO EDIT\n\n"
        "Send your photo with your editing requirement.",

        "video":
        "🎬 VIDEO EDIT\n\n"
        "Tell me your video editing idea.",

        "poster":
        "🖼️ POSTER MAKER\n\n"
        "Tell me your poster topic.",

        "caption":
        "✍️ CAPTION + HASHTAGS\n\n"
        "Send your post or reel topic.",

        "ideas":
        "💡 CONTENT IDEAS\n\n"
        "Tell me your content category."
    }

    await query.message.reply_text(messages[query.data])


# =========================
# PHOTO UPLOAD
# =========================

async def photo_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):

    caption = update.message.caption

    if not caption:
        caption = "HD cinematic DSLR edit"

    prompt = (
        "🎨 KATHU 764 PHOTO EDIT PROMPT\n\n"

        f"Requirement:\n{caption}\n\n"

        "Edit this uploaded photo professionally.\n\n"

        "✨ HD + HDR quality\n"
        "🎨 Cinematic colour grading\n"
        "📷 Professional DSLR look\n"
        "✨ Sharp and clean details\n"
        "🌟 Natural skin tones\n"
        "💡 Balanced exposure and lighting\n"
        "🎬 Premium cinematic finish\n\n"

        "Important:\n"
        "Preserve the original face, identity, "
        "clothes, jewellery, pose and important details.\n\n"

        "Do not over-edit the face or change the person's identity."
    )

    await update.message.reply_text(prompt)


# =========================
# TEXT MESSAGE HANDLER
# =========================

async def text_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = update.message.text

    mode = context.user_data.get("mode")

    if mode == "photo":

        reply = (
            "🎨 PHOTO EDIT PROMPT\n\n"

            "Create a professional photo edit based on:\n"
            f"{text}\n\n"

            "Use HD + HDR quality, cinematic colour grading, "
            "natural skin tones, sharp details, DSLR look, "
            "balanced lighting and premium finish.\n\n"

            "Preserve the original face, identity, clothes "
            "and important details."
        )

    elif mode == "video":

        reply = (
            "🎬 VIDEO EDIT PROMPT\n\n"

            f"Create a cinematic video edit based on:\n{text}\n\n"

            "Use smooth transitions, clear voice, "
            "balanced background music, HD quality, "
            "cinematic colour grading and engaging pacing."
        )

    elif mode == "poster":

        reply = (
            "🖼️ POSTER PROMPT\n\n"

            f"Create a premium Instagram poster based on:\n{text}\n\n"

            "Use cinematic lighting, clean composition, "
            "bold readable typography, HD quality "
            "and professional colour grading."
        )

    elif mode == "caption":

        reply = (
            "✍️ CAPTION + HASHTAGS\n\n"

            f"Topic: {text}\n\n"

            "🔥 Create a short catchy caption.\n"
            "#Instagram #Reels #Creator #Kathu764"
        )

    elif mode == "ideas":

        reply = (
            "💡 CONTENT IDEAS\n\n"

            f"Category: {text}\n\n"

            "1️⃣ Trending Reel\n"
            "2️⃣ Before / After Edit\n"
            "3️⃣ Quick Tutorial\n"
            "4️⃣ Behind The Scenes\n"
            "5️⃣ Creator Tips\n"
            "6️⃣ Photo Editing Reel\n"
            "7️⃣ Viral Hook Video"
        )

    else:

        reply = (
            "🔥 KATHU 764 CREATOR BOT\n\n"
            "Use /start to open the main menu."
        )

    await update.message.reply_text(reply)


# =========================
# HELP
# =========================

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(
        "🆘 KATHU 764 CREATOR BOT\n\n"
        "/start - Open Menu\n"
        "/photo - Photo Edit\n"
        "/video - Video Edit\n"
        "/poster - Poster Maker\n"
        "/caption - Caption + Hashtags\n"
        "/ideas - Content Ideas"
    )


# =========================
# MAIN
# =========================

def main():

    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))

    app.add_handler(CommandHandler("photo", photo_command))
    app.add_handler(CommandHandler("video", video_command))
    app.add_handler(CommandHandler("poster", poster_command))
    app.add_handler(CommandHandler("caption", caption_command))
    app.add_handler(CommandHandler("ideas", ideas_command))

    app.add_handler(CallbackQueryHandler(buttons))

    # PHOTO HANDLER
    app.add_handler(
        MessageHandler(filters.PHOTO, photo_handler)
    )

    # TEXT HANDLER
    app.add_handler(
        MessageHandler(
            filters.TEXT & ~filters.COMMAND,
            text_handler
        )
    )

    print("🔥 KATHU 764 CREATOR BOT is running...")

    app.run_polling()


if __name__ == "__main__":
    main()
