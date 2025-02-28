# Folosim o imagine de bază oficială pentru Python
FROM python:3.8-slim

# Setăm directorul de lucru
WORKDIR /app

# Copiem fișierele necesare din repository în container
COPY . /app

# Instalăm dependențele (presupunem că ai un fișier requirements.txt)
RUN pip install -r requirements.txt

# Expunem portul pe care va rula aplicația
EXPOSE 5000

# Comanda pentru a lansa aplicația (presupunând că ai un fișier app.py)
CMD ["python", "app.py"]
