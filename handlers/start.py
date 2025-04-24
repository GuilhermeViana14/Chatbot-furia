from telegram import Update
from telegram.ext import CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Salve, fã da FURIA! \U0001F40D\nUse os comandos:\n"
        "/proximos - Ver próximos jogos\n"
        "/resultados - Ver últimos resultados\n"
        "/stats <jogador> - Stats do jogador\n"
        "/tweets - Últimos tweets da FURIA"
    )

start_handler = CommandHandler("start", start)
