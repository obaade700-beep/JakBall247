import os
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

# Logging for debugging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, 
                                   text="Welcome to JakBall247! Use /trivia or /schedule to get started.")

async def trivia(update: Update, context: ContextTypes.DEFAULT_TYPE):
    fact = "Did you know? The most popular sport in the world is Football (Soccer), with over 3.5 billion fans globally."
    await context.bot.send_message(chat_id=update.effective_chat.id, text=fact)

async def schedule(update: Update, context: ContextTypes.DEFAULT_TYPE):
    info = "Upcoming Matches:\n1. Man City vs Liverpool - Saturday 5 PM\n2. Real Madrid vs Barca - Sunday 8 PM"
    await context.bot.send_message(chat_id=update.effective_chat.id, text=info)

if __name__ == '__main__':
    # Get your token from environment variables (Set this in Railway)
    TOKEN = os.environ.get("BOT_TOKEN")
    
    application = ApplicationBuilder().token(TOKEN).build()
    
    # Handlers
    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('trivia', trivia))
    application.add_handler(CommandHandler('schedule', schedule))
    
    print("Bot is running...")
    application.run_polling()
