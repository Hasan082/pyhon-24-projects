from token_file import TOKEN, BOT_USERNAME
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes, Updater


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello there, Nice to meet you! Let\'s chat")


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Get help with commands and features")


async def about_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "I'm a simple Telegram bot created for learning purposes. "
        "I can currently perform basic tasks like providing weather updates and news headlines. "
        "I'm still under development, so expect more features in the future!"
    )


async def weather_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Today\'s weather is sunny and warm!")


async def news_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Do you like to see today's news?")


async def todo_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Do you like to make a todo list for you?")


async def schedule_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Would you like to make a schedule list for you?")


async def joke_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Would you like to make a joke?")


async def quote_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Would you like to make a quote?")


def handle_response(text: str):
    processed: str = text.lower()

    if 'hello' in processed:
        return f"Hello There"

    if 'how are you' in processed:
        return f"I am good, thanks!"

    if 'i love python' in processed:
        return f"Python is coooooooool!!!!"

    if 'i love you' in processed:
        return f"You\'re love, thanks!"

    if 'mukta' in processed:
        return f"You\'re mukta, thanks!"

    if 'hi' in processed:
        return f"Hello there, thanks!"

    if 'good morning' in processed:
        return f"Good morning to you too!"

    if 'good afternoon' in processed:
        return f"good afternoon, thanks!"

    if 'good evening' in processed:
        return f"Good evening to you too!"

    if 'good night' in processed:
        return f"Good night to you too!"

    if 'what\'s up' in processed:
        return f"Just coding, not kidding..!"

    if 'thanks' in processed:
        return f"You are Welcome!"

    if 'thank you' in processed:
        return f"No Problem!"

    if 'bye' in processed:
        return f"Bye"

    return "Your question is out of my memory!"


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type = update.message.chat.type
    text: str = update.message.text

    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, "").strip()
            response = handle_response(new_text)
        else:
            return
    else:
        response = handle_response(text)

    # Reply
    print("Bot", response)

    await update.message.reply_text(response)


async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f"Update {update} caused error {context.error}")


def main():
    print("Starting bot...")
    app = Application.builder().token(TOKEN).build()

    #Commands
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("about", about_command))
    app.add_handler(CommandHandler("weather", weather_command))
    app.add_handler(CommandHandler("news", news_command))
    app.add_handler(CommandHandler("schedule", schedule_command))
    app.add_handler(CommandHandler("joke", joke_command))
    app.add_handler(CommandHandler("quote", quote_command))

    # Message
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # Error
    app.add_error_handler(error_handler)

    print("Bot started")
    app.run_polling(poll_interval=5)


if __name__ == "__main__":
    main()
