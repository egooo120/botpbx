from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# IDs de usuarios admin y normales
ADMINS = {7279435741}            # Reemplaza con IDs reales de admins
NORMAL_USERS = {7469232318 }  # IDs de usuarios normales

# Diccionario para almacenar saldo
user_saldos = {}

async def prueba(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if user_id in ADMINS or user_id in NORMAL_USERS:
        await update.message.reply_text("OK")
    else:
        await update.message.reply_text("Unauthorized")

async def saldomas(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if user_id not in ADMINS:
        await update.message.reply_text("Unauthorized — solo admins pueden usar este comando.")
        return

    if len(context.args) != 2:
        await update.message.reply_text("Uso: /saldomas <id_usuario> <cantidad>")
        return

    try:
        target_id = int(context.args[0])
        amount = float(context.args[1])
    except ValueError:
        await update.message.reply_text("ID o cantidad inválidos. Deben ser números.")
        return

    saldo_actual = user_saldos.get(target_id, 0)
    user_saldos[target_id] = saldo_actual + amount

    await update.message.reply_text(f"Saldo del usuario {target_id} actualizado a {user_saldos[target_id]:.2f}")

async def saldo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if user_id not in ADMINS and user_id not in NORMAL_USERS:
        await update.message.reply_text("Unauthorized")
        return

    if len(context.args) != 2:
        await update.message.reply_text("Uso correcto: /saldo <id_usuario> <cantidad>")
        return

    try:
        target_id = int(context.args[0])
        amount = float(context.args[1])
    except ValueError:
        await update.message.reply_text("ID o cantidad inválidos. Deben ser números.")
        return

    saldo_actual = user_saldos.get(target_id, 0)
    user_saldos[target_id] = saldo_actual + amount

    await update.message.reply_text(f"Saldo de usuario {target_id} actualizado a {user_saldos[target_id]:.2f}")

if __name__ == "__main__":
    app = ApplicationBuilder().token("7888426082:AAEXYCA5nLXliYys6vcursz1qNHlSJ3cRs0").build() #TOKENBOT

    app.add_handler(CommandHandler("prueba", prueba))
    app.add_handler(CommandHandler("saldo", saldo))
    app.add_handler(CommandHandler("saldomas", saldomas))

    app.run_polling()
