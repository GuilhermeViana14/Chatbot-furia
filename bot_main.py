from telegram.ext import ApplicationBuilder
from handlers.start import start_handler
from handlers.proximos import proximos_handler
from handlers.resultados import resultados_handler
from handlers.stats import stats_handler
from handlers.tweets import tweets_handler
from config import TELEGRAM_TOKEN

app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
app.add_handler(start_handler)
app.add_handler(proximos_handler)
app.add_handler(resultados_handler)
app.add_handler(stats_handler)
app.add_handler(tweets_handler)

app.run_polling()