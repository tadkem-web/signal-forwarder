print("🟢 Programa paleista sėkmingai!")
print("Tikrinama telethon biblioteka...")
try:
    import telethon
    print("✅ telethon biblioteka veikia")
except ImportError as e:
    print(f"❌ Klaida: {e}")

print("Tikrinama aplinkos kintamuosius...")
import os
try:
    keys = ['API_ID', 'API_HASH', 'SESSION_STRING', 'BOT_TOKEN', 'TARGET_CHANNEL_ID']
    for key in keys:
        value = os.environ.get(key)
        if value:
            print(f"✅ {key}: {len(value)} simbolių")
        else:
            print(f"❌ {key}: NERASTAS")
except Exception as e:
    print(f"❌ Klaida: {e}")
