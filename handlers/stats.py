from telegram import Update
from telegram.ext import CommandHandler, ContextTypes

async def stats(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("Use assim: /stats yuurih")
        return
    jogador = context.args[0]
    msg = f"Stats de {jogador} (mock):\nRating: 1.18\nK/D: 1.21\nHeadshots: 56%"
    await update.message.reply_text(msg)


stats_handler = CommandHandler("stats", stats)
