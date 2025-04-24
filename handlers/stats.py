from telegram import Update
from telegram.ext import CommandHandler, ContextTypes
# Dicionário de jogadores e seus respectivos IDs
jogadores_ids = {
    "kscerato": "15631",
    "yuurih": "12553",
    "fallen": "2023",
    "molodoy": "24144",
    "yekindar": "13915",
}

# Função para redirecionar o usuário para a página de estatísticas de um jogador
async def stats(update, context):
    jogador = ' '.join(context.args).lower()  # Pega o nome do jogador a partir do comando
    
    # Verifica se o jogador está no dicionário
    if jogador in jogadores_ids:
        id_jogador = jogadores_ids[jogador]
        url = f"https://www.hltv.org/stats/players/{id_jogador}/{jogador}"
        await update.message.reply_text(f"Veja as estatísticas do jogador {jogador} aqui: {url}")
    else:
        await update.message.reply_text("Jogador não encontrado. Tente novamente com o nome correto.")

# Handler para o comando /stats
stats_handler = CommandHandler("stats", stats)