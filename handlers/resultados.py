from telegram import Update
from telegram.ext import CommandHandler, ContextTypes

async def resultados(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = "Últimos resultados:\nFURIA 16 x 10 ENCE\nFURIA 12 x 16 Vitality"
    await update.message.reply_text(msg)

resultados_handler = CommandHandler("resultados", resultados)
