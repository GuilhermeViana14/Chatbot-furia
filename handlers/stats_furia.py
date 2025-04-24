from telegram import Update
from telegram.ext import CommandHandler, ContextTypes

from telegram.ext import CommandHandler

# Função para redirecionar o usuário para a página de estatísticas da FURIA
async def stats_furia(update, context):
    url = "https://www.hltv.org/team/8297/furia"
    await update.message.reply_text(f"Veja as estatísticas da FURIA aqui: {url}")

# Handler para o comando /stats_furia
stats_furia_handler = CommandHandler("status_furia", stats_furia)

