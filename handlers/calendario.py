from telegram import Update
from telegram.ext import CommandHandler, ContextTypes
from components.furia_matches import get_furia_matches

async def calendario(update, context):
    jogos_futuros = get_furia_matches()  # Pegando os jogos futuros da FURIA

    if jogos_futuros and jogos_futuros != "Nenhum jogo futuro encontrado para a FURIA.":
        # Envia cada jogo encontrado como uma mensagem
        for jogo in jogos_futuros.splitlines():  # divide as linhas
            await update.message.reply_text(jogo)
    else:
        await update.message.reply_text(jogos_futuros)  # Caso não haja jogos, a função já retorna uma mensagem adequada.


calendario_handler = CommandHandler("calendario", calendario)
