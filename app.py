print("🟢 Programa paleista su 512MB RAM!")
print("Tikrinami kintamieji...")

import os
import time

# Tikriname, ar visi kintamieji egzistuoja
required_vars = ['API_ID', 'API_HASH', 'BOT_TOKEN', 'TARGET_CHANNEL_ID', 'SESSION_STRING']

for var in required_vars:
    value = os.environ.get(var)
    if value:
        print(f"✅ {var}: {value[:3]}...")
    else:
        print(f"❌ {var}: NERASTAS")

print("Miegama 2 minutes, kad galėtumėte pamatyti log'us...")
time.sleep(120)
print("Programa baigia darbą.")
