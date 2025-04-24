from telegram import Update
from telegram.ext import CommandHandler, ContextTypes

async def tweets(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = "Venha ver os ultimos tweets da FURIA! \U0001F426\n\n"
    msg += "https://x.com/FURIA?ref_src=twsrc%5Egoogle%7Ctwcamp%5Eserp%7Ctwgr%5Eauthor"
    await update.message.reply_text(msg)

tweets_handler = CommandHandler("tweets", tweets)
