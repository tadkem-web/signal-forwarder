# Naudosime oficialų Python 3.10 atvaizdą
FROM python:3.10-slim

# Nustatome darbo katalogą
WORKDIR /app

# Įkeliame reikalavimų failą ir įdiegiame priklausomybes
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Įkeliame visą projektą
COPY . .

# Nustatome komandą, kuri bus paleista startuojant
CMD ["python", "main.py"]
