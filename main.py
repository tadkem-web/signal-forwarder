import os
import re
from telethon import TelegramClient, events

# API raktai (Railway → Variables)
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")
SOURCE_CHAT = os.getenv("SOURCE_CHAT")   # signalų grupė (pvz. @Signal_Messenger8)
TARGET_CHAT = os.getenv("TARGET_CHAT")   # tavo kanalo ID (-100...)

client = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN)

@client.on(events.NewMessage(chats=SOURCE_CHAT))
async def handler(event):
    message = event.raw_text
    # Ieškome Leverage reikšmių
    match = re.search(r'Leverage\s*[:：]?\s*x?(\d+)', message, re.IGNORECASE)
    if match:
        lev = int(match.group(1))
        if lev >= 9:  # Filtruojame signalus nuo 9x
            await client.send_message(TARGET_CHAT, message)

print("🚀 Botas paleistas ir laukia signalų...")
client.run_until_disconnected()
