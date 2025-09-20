import os
from telethon import TelegramClient, events

# API ir bot token gaunami iš Fly.io secrets
api_id = int(os.getenv("TG_API_ID"))
api_hash = os.getenv("TG_API_HASH")
bot_token = os.getenv("TG_BOT_TOKEN")

# Sukuriam klientą su bot token
client = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)

# 🔴 ČIA SUDEDU TAVO KANALŲ ID 🔴
SOURCE_CHAT = -1001234567890      # signalų grupės chat_id
TARGET_CHAT = -1002539410010      # tavo kanalo "Prekybos signalai" chat_id

print("🚀 Forwarderis paleistas – laukiu žinučių...")

@client.on(events.NewMessage(chats=SOURCE_CHAT))
async def handler(event):
    try:
        await client.send_message(TARGET_CHAT, event.message)
        print("✅ Persiųsta žinutė")
    except Exception as e:
        print("❌ Klaida:", e)

client.run_until_disconnected()
