from telegram import Update
from telegram.ext import CommandHandler, ContextTypes

async def tweets(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = "Últimos tweets da FURIA:\n1. FURIA avança para os playoffs!\n2. Nova line feminina anunciada!\n3. Próximo jogo contra NAVI, vamos com tudo!"
    await update.message.reply_text(msg)

tweets_handler = CommandHandler("tweets", tweets)
