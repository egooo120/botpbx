from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Lista de usuarios autorizados
AUTHORIZED_USERS = {7469232318, 7279435741}  # Pon aquí los IDs autorizados

async def prueba(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if user_id in AUTHORIZED_USERS:
        await update.message.reply_text("OK")
    else:
        await update.message.reply_text("Unauthorized")

async def main():
    app = ApplicationBuilder().token("7888426082:AAEXYCA5nLXliYys6vcursz1qNHlSJ3cRs0").build()
    app.add_handler(CommandHandler("prueba", prueba))
    await app.run_polling()

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
