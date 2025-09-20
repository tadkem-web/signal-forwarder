import os
import re
from telethon import TelegramClient, events

# API ID ir API HASH pasiimti iš my.telegram.org
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")

# Telegram sesijos failo vardas
SESSION = "forwarder"

# Šaltinio grupės username
SOURCE_CHAT = "@Signal_Messenger8"

# Tik šio autoriaus (nario) ID klausom
SOURCE_USER = 274148621

# Tikslinis kanalas, į kurį siųsim žinutes
TARGET_CHAT = -1002539410010

client = TelegramClient(SESSION, API_ID, API_HASH)

@client.on(events.NewMessage(chats=SOURCE_CHAT, from_users=SOURCE_USER))
async def handler(event):
    text = event.raw_text

    # Ieškom leverage reikšmės
    match = re.search(r"Leverage\s*:?[\s]*([0-9]+)", text, re.IGNORECASE)
    if match:
        lev = int(match.group(1))
        if lev >= 3:  # tik jeigu >=3
            await client.send_message(TARGET_CHAT, text)

print("🚀 Forwarderis paleistas...")
client.start()
client.run_until_disconnected()
