import os
import re
from telethon import TelegramClient, events

# Secrets
api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")
source_chat = int(os.getenv("SOURCE_CHAT_ID"))   # signalų grupė
target_chat = int(os.getenv("TARGET_CHAT_ID"))   # tavo kanalas

client = TelegramClient("forwarder", api_id, api_hash)

@client.on(events.NewMessage(chats=source_chat))
async def handler(event):
    text = event.message.message

    # Ieškom "Leverage" + skaičius
    match = re.search(r"Leverage\s*[:\-]?\s*(\d+)", text, re.IGNORECASE)
    if match:
        leverage = int(match.group(1))
        if leverage >= 3:
            await client.send_message(target_chat, text)
            print(f"✅ Persiųsta (Leverage {leverage})")
        else:
            print(f"❌ Praleista (Leverage {leverage})")
    else:
        print("⚠️ Nerasta 'Leverage' žinutėje, praleista.")

print("🚀 Forwarderis paleistas...")
client.start()
client.run_until_disconnected()
