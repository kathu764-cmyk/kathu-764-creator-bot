import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

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
        "Welcome! Choose an option below 👇",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


async def buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    messages = {
        "photo": "🎨 Send me your photo editing requirement.",
        "video": "🎬 Send me your video editing idea.",
        "poster": "🖼️ Tell me your poster topic.",
        "caption": "✍️ Tell me your post or reel topic.",
        "ideas": "💡 Tell me your content category."
    }

    await query.message.reply_text(messages[query.data])


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🆘 KATHU 764 CREATOR BOT\n\n"
        "Use /start to open the main menu."
    )


def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CallbackQueryHandler(buttons))

    print("🔥 KATHU 764 CREATOR BOT is running...")
    app.run_polling()


if __name__ == "__main__":
    main()
