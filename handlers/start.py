from telegram import Update
from telegram.ext import CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Salve, fã da FURIA! \U0001F40D\nUse os comandos:\n"
        "/stats <jogador> - Stats do jogador\n"
        "/tweets - Últimos tweets da FURIA\n"
        "/calendario - Ver o calendário de jogos\n"
        "/status_furia - Stats da FURIA\n"
    )

start_handler = CommandHandler("start", start)
