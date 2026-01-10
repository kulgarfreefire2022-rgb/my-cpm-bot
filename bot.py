from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import subprocess

# Masukkan TOKEN dari BotFather
TOKEN = "8206837693:AAGQB86CiT7g2wZOFg73daDA4Jg4MMZWE8c"

def start(update: Update, context: CallbackContext):
    update.message.reply_text("Bot CPM aktif! Gunakan /rank_cpm1 atau /rank_cpm2")

def rank_cpm1(update: Update, context: CallbackContext):
    update.message.reply_text("Menjalankan CPM1...")
    # jalankan script cpm1.py
    result = subprocess.getoutput("python cpm1.py")
    update.message.reply_text(f"Hasil CPM1:\n{result}")

def rank_cpm2(update: Update, context: CallbackContext):
    update.message.reply_text("Menjalankan CPM2...")
    # jalankan script cpm2.py
    result = subprocess.getoutput("python cpm2.py")
    update.message.reply_text(f"Hasil CPM2:\n{result}")

def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("rank_cpm1", rank_cpm1))
    dp.add_handler(CommandHandler("rank_cpm2", rank_cpm2))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
