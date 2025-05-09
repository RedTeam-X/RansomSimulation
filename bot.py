import os
import json
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Load level data from JSON
with open("ransomware_levels.json", "r") as f:
    levels = json.load(f)

def get_level(level_id):
    for lvl in levels:
        if lvl["id"] == level_id:
            return lvl
    return None

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Selamat datang di Ransomware Simulation Bot!\n"
        "Ketik /level [nomor] untuk memilih level.\nContoh: /level 1"
    )

async def level(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) == 0:
        await update.message.reply_text("Gunakan: /level [nomor]. Contoh: /level 3")
        return

    try:
        level_id = int(context.args[0])
        lvl = get_level(level_id)
        if lvl:
            msg = (
                f"🔥 Level {lvl['id']}: {lvl['name']}\n"
                f"Kesulitan: {lvl['difficulty']}\n\n"
                f"{lvl['description']}\n\n"
                f"Tugas:\n{lvl['goal']}"
            )
            await update.message.reply_text(msg)
        else:
            await update.message.reply_text("Level tidak ditemukan.")
    except ValueError:
        await update.message.reply_text("Gunakan angka sebagai ID level.")

if __name__ == "__main__":
    token = os.environ.get("7596809034:AAEhBKNUe8HLbtafAgZgmkcBYVJdhxIgB3I")
    app = ApplicationBuilder().token(token).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("level", level))
    print("Bot berjalan...")
    app.run_polling()
