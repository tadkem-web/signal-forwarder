import os
import logging
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

logging.basicConfig(level=logging.INFO)

BOT_TOKEN = os.getenv("BOT_TOKEN")

# Tavo ID
SOURCE_CHAT_ID = 274148621        # Signal Messenger narys
TARGET_CHAT_ID = -1002539410010   # Kanalas „Prekybos signalai“

async def forward_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_chat.id == SOURCE_CHAT_ID:
        await context.bot.forward_message(
            chat_id=TARGET_CHAT_ID,
            from_chat_id=update.effective_chat.id,
            message_id=update.message.message_id
        )
        logging.info("Persiųsta į kanalą")

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.ALL, forward_message))
    app.run_polling()

if __name__ == "__main__":
    main()
