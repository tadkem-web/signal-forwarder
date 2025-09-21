FROM python:3.11-slim-buster

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# 🟢 DIAGNOSTIKA: Patikriname, ar įdiegiamos bibliotekos
CMD ["python", "-c", "\n\
import os\n\
print('= = = = = DIAGNOSTIKA PRASIDEDA = = = = =')\n\
\n\
# 1. Tikriname bibliotekas\n\
try:\n\
    import telethon\n\
    print('✅ Telethon biblioteka įdiegta sėkmingai')\n\
except ImportError as e:\n\
    print(f'❌ Telethon importo klaida: {e}')\n\
\n\
# 2. Tikriname aplinkos kintamuosius\n\
print('\\\\n--- Aplinkos kintamieji ---')\n\
required_vars = ['API_ID', 'API_HASH', 'BOT_TOKEN', 'TARGET_CHANNEL_ID', 'SESSION_STRING']\n\
for var in required_vars:\n\
    value = os.environ.get(var)\n\
    if value:\n\
        print(f'✅ {var}: {value[:5]}...')\n\
    else:\n\
        print(f'❌ {var}: NERASTAS')\n\
\n\
print('= = = = = DIAGNOSTIKA BAIGIASI = = = = =')\n\
"]
