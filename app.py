print("🟢 Python programa paleista!")
print("Tikrinama, ar visi kintamieji egzistuoja...")

import os
import time

required_vars = ['API_ID', 'API_HASH', 'BOT_TOKEN', 'TARGET_CHANNEL_ID', 'SESSION_STRING']

for var in required_vars:
    value = os.environ.get(var)
    if value:
        print(f"✅ {var}: {value[:3]}...")
    else:
        print(f"❌ {var}: NERASTAS")

print("Miegama 2 minutes...")
time.sleep(120)
print("Programa baigia darbą.")
