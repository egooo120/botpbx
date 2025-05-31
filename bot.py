import asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# ID de usuario autorizado
AUTHORIZED_USERS = {7279435741}  # Reemplaza con tu ID de Telegram

# Comando /prueba
async def prueba(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if user_id in AUTHORIZED_USERS:
        await update.message.reply_text("OK")
    else:
        await update.message.reply_text("Unauthorized")

# Función principal
async def main():
    app = ApplicationBuilder().token("7888426082:AAEXYCA5nLXliYys6vcursz1qNHlSJ3cRs0").build()
    app.add_handler(CommandHandler("prueba", prueba))
    await app.run_polling()

# Lanzamiento seguro
if __name__ == '__main__':
    try:
        loop = asyncio.get_event_loop()
        if loop.is_running():
            loop.create_task(main())
        else:
            loop.run_until_complete(main())
    except RuntimeError:
        new_loop = asyncio.new_event_loop()
        asyncio.set_event_loop(new_loop)
        new_loop.run_until_complete(main())
