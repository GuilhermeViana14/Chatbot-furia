from telegram.ext import ApplicationBuilder
from handlers.start import start_handler
from handlers.stats import stats_handler
from handlers.tweets import tweets_handler
from handlers.stats_furia import stats_furia_handler
from handlers.calendario import calendario_handler

# Substitua com seu token diretamente
TELEGRAM_TOKEN = "7952260234:AAELsuQhusnYuelyQm7H-yr3XcOPsOA5Y1k"

# Inicializa a aplicação do bot
app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

# Adiciona os handlers
app.add_handler(start_handler)
app.add_handler(stats_handler)
app.add_handler(tweets_handler)
app.add_handler(stats_furia_handler)
app.add_handler(calendario_handler)

# Inicia o bot com polling
app.run_polling()
