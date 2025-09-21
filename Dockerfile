# Naudojame oficialų Python image
FROM python:3.11-slim-buster

# Nustatome darbinį katalogą
WORKDIR /app

# Nukopijuojame reikalavimų failą ir įdiegiame priklausomybes
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Nukopijuojame pagrindinį programos failą
COPY app.py .

# Paleidžiame programą
CMD ["python", "-u", "app.py"]
