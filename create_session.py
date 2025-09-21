# create_session.py
from telethon import TelegramClient
from telethon.sessions import StringSession
import asyncio

async def main():
    api_id = input("API_ID: ").strip()
    api_hash = input("API_HASH: ").strip()
    client = TelegramClient(StringSession(), api_id, api_hash)
    await client.start()
    print("=== SUKURTAS STRING SESSION ===")
    print(StringSession.save(client.session))
    await client.disconnect()

if __name__ == "__main__":
    asyncio.run(main())
