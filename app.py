import os
import asyncio
from telethon import TelegramClient, events
from telethon.sessions import StringSession

# ========== KONFIGŪRACIJA IS FLY.IO KINTAMUJU ==========
api_id = int(os.environ['API_ID'])
api_hash = os.environ['API_HASH']
session_string = os.environ['SESSION_STRING']
bot_token = os.environ['BOT_TOKEN']
target_channel_id = int(os.environ['TARGET_CHANNEL_ID'])
# =======================================================

print("Pradedama signalų persiuntimo programa...")

# Inicializuojame klienta (jūsų vartotojo paskyra)
client = TelegramClient(StringSession(session_string), api_id, api_hash)
# Inicializuojame botą (žinučių siuntėjas)
bot = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)

# Jūsų signalų grupės ID: 274148621
SOURCE_CHAT_ID = 274148621

@client.on(events.NewMessage(chats=SOURCE_CHAT_ID))
async def handler(event):
    msg_text = event.message.text
    print(f"Gauta žinutė: {msg_text[:100]}...")  # Log'ui

    # Tikriname, ar žinutėje yra "Leverage: x" ir skaičius >= 3
    if "Leverage: x" in msg_text:
        try:
            # Išskiriame leverage reikšmę
            parts = msg_text.split("Leverage: x")
            leverage_value = int(parts[1].split()[0].strip())  # Paimame pirmą skaičių po 'x'

            if leverage_value >= 3:
                print(f"✅ Aptiktas tinkamas signalas su Leverage: x{leverage_value}")
                # Persiunčiame originalią žinutę į kanalą naudodami BOTĄ
                async with bot:
                    await bot.send_message(
                        entity=target_channel_id,
                        message=f"🚨 **SVARBUS SIGNALAS** 🚨\n\n{msg_text}"
                    )
                print("✅ Signalas sėkmingai persiųstas į kanalą!")

        except (IndexError, ValueError, Exception) as e:
            print(f"❌ Klaida apdorojant žinutę: {e}")

async def main():
    await client.start()
    print("Programa paleista ir klausosi žinučių grupėje...")
    await client.run_until_disconnected()

if __name__ == '__main__':
    asyncio.run(main())
