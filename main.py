# main.py
import os
import asyncio
from telethon import TelegramClient, events
from telethon.sessions import StringSession

API_ID = int(os.environ.get("API_ID", "0"))
API_HASH = os.environ.get("API_HASH", "")
STRING_SESSION = os.environ.get("STRING_SESSION", "")
SOURCE_CHAT = os.environ.get("SOURCE_CHAT", "")  # can be numeric id or '@username'
TARGET_CHAT = os.environ.get("TARGET_CHAT", "")  # channel id or '@channelusername'

if not (API_ID and API_HASH and STRING_SESSION and SOURCE_CHAT and TARGET_CHAT):
    print("Missing env vars. Please set API_ID, API_HASH, STRING_SESSION, SOURCE_CHAT, TARGET_CHAT.")
    raise SystemExit(1)

client = TelegramClient(StringSession(STRING_SESSION), API_ID, API_HASH,)

@client.on(events.NewMessage(chats=SOURCE_CHAT))
async def handler(event):
    try:
        msg = event.message
        # forward preserving original sender + media if any:
        if msg.media:
            await client.send_file(TARGET_CHAT, msg.media, caption=msg.text or "")
        else:
            await client.send_message(TARGET_CHAT, msg.text or "")
        print("Forwarded message id", msg.id)
    except Exception as e:
        print("Error forwarding:", repr(e))

async def main_loop():
    print("Starting client...")
    await client.start()
    print("Client started, listening for messages from", SOURCE_CHAT, "->", TARGET_CHAT)
    await client.run_until_disconnected()

if __name__ == "__main__":
    asyncio.run(main_loop())
