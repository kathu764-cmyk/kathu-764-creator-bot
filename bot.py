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


async def photo_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["mode"] = "photo"
    await update.message.reply_text(
        "🎨 PHOTO EDIT MODE\n\n"
        "Tell me what edit you want.\n\n"
        "Example:\n"
        "HD + HDR + cinematic colour grading + DSLR look"
    )


async def video_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["mode"] = "video"
    await update.message.reply_text(
        "🎬 VIDEO EDIT MODE\n\n"
        "Tell me your video editing idea."
    )


async def poster_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["mode"] = "poster"
    await update.message.reply_text(
        "🖼️ POSTER MODE\n\n"
        "Tell me the poster topic and size."
    )


async def caption_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["mode"] = "caption"
    await update.message.reply_text(
        "✍️ CAPTION MODE\n\n"
        "Send your post/reel topic."
    )


async def ideas_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["mode"] = "ideas"
    await update.message.reply_text(
        "💡 CONTENT IDEAS MODE\n\n"
        "Tell me your content category."
    )


async def buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    context.user_data["mode"] = query.data

    messages = {
        "photo": "🎨 Send your photo editing requirement.",
        "video": "🎬 Send your video editing idea.",
        "poster": "🖼️ Tell me your poster topic.",
        "caption": "✍️ Tell me your post or reel topic.",
        "ideas": "💡 Tell me your content category."
    }

    await query.message.reply_text(messages[query.data])


async def text_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    mode = context.user_data.get("mode")

    if mode == "photo":
        reply = (
            "🎨 PHOTO EDIT PROMPT\n\n"
            "Edit the uploaded photo professionally with HD quality, "
            "HDR enhancement, cinematic colour grading, natural skin tones, "
            "sharp details, DSLR look, balanced exposure and premium finish. "
            "Preserve the original face, identity, clothes and important details."
        )

    elif mode == "video":
        reply = (
            "🎬 VIDEO EDIT PROMPT\n\n"
            f"Create a cinematic professional edit based on: {text}\n\n"
            "Use smooth transitions, clear voice, balanced background audio, "
            "HD quality and engaging pacing."
        )

    elif mode == "poster":
        reply = (
            "🖼️ POSTER PROMPT\n\n"
            f"Create a premium Instagram poster based on: {text}\n\n"
            "Use clean composition, bold readable typography, cinematic "
            "lighting, HD quality and professional colour grading."
        )

    elif mode == "caption":
        reply = (
            "✍️ CAPTION + HASHTAGS\n\n"
            f"Topic: {text}\n\n"
            "🔥 Create a short catchy caption with relevant hashtags."
        )

    elif mode == "ideas":
        reply = (
            "💡 CONTENT IDEAS\n\n"
            f"Category: {text}\n\n"
            "1. Trending Reel\n"
            "2. Before / After Edit\n"
            "3. Quick Tutorial\n"
            "4. Behind The Scenes\n"
            "5. Creator Tips"
        )

    else:
        reply = (
            "🔥 KATHU 764 CREATOR BOT\n\n"
            "Use /start and choose an option."
        )

    await update.message.reply_text(reply)


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🆘 Use /start to open the KATHU 764 CREATOR menu."
    )


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
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, text_handler))

    print("🔥 KATHU 764 CREATOR BOT is running...")
    app.run_polling()


if __name__ == "__main__":
    main()
