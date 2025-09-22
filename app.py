print("🟢 Programa paleista sėkmingai!")
print("Tikrinama, ar visi kintamieji yra...")

import os

required_vars = ['API_ID', 'API_HASH', 'BOT_TOKEN', 'TARGET_CHANNEL_ID', 'SESSION_STRING']
all_vars_exist = True

for var in required_vars:
    value = os.environ.get(var)
    if value:
        print(f"✅ {var}: {value[:3]}...")
    else:
        print(f"❌ {var}: NERASTAS")
        all_vars_exist = False

if all_vars_exist:
    print("🎉 Visi kintamieji egzistuoja! Programa veiktų.")
else:
    print("💥 Trūksta kintamųjų! Programa užsidarys.")
    exit(1)
