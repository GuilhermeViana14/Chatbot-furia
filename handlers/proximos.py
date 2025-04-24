from telegram import Update
from telegram.ext import CommandHandler, ContextTypes

async def proximos(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = "Próximos jogos da FURIA:\n1. FURIA vs NAVI - 25/04\n2. FURIA vs G2 - 27/04"
    await update.message.reply_text(msg)

proximos_handler = CommandHandler("proximos", proximos)