import os
import re
from telethon import TelegramClient, events

# Aplinkos kintamieji (Fly secrets)
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
SOURCE_CHAT_ID = int(os.getenv("SOURCE_CHAT_ID"))
TARGET_CHAT_ID = int(os.getenv("TARGET_CHAT_ID"))

# Sesija laikoma atmintyje, nereikia prisijungimo iš naujo
client = TelegramClient("forwarder", API_ID, API_HASH)

# Regex paimti Leverage reikšmei
LEVERAGE_REGEX = re.compile(r"\b(\d+)\s*[xX]|\bLeverage[: ]+(\d+)", re.IGNORECASE)

def extract_leverage(text: str) -> int:
    match = LEVERAGE_REGEX.search(text)
    if match:
        return int(match.group(1) or match.group(2))
    return 1

@client.on(events.NewMessage(chats=SOURCE_CHAT_ID))
async def handler(event):
    msg_text = event.message.message or ""
    lev = extract_leverage(msg_text)
    if lev >= 3:
        await client.send_message(TARGET_CHAT_ID, event.message)

print("🚀 Forwarderis paleistas... Laukiu žinučių.")

client.start()
client.run_until_disconnected()
