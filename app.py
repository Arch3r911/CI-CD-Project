from flask import Flask
from prometheus_client import start_http_server, Summary
import random
import time

# Creăm aplicația Flask
app = Flask(__name__)

# Definim o metrică pentru timpul de execuție al unei funcții
REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')

# Endpoint pentru a expune metricile Prometheus
@app.route("/metrics")
def metrics():
    # Expunem metricile într-un format pe care Prometheus îl poate citi
    from prometheus_client import generate_latest
    return generate_latest()

# Funcție pentru a simula un proces de lungă durată
@REQUEST_TIME.time()  # Această decoratoare va măsura timpul de execuție
def process_request():
    # Simulăm o întârziere
    time.sleep(random.uniform(0.1, 1.0))  # Întârziere aleatorie între 0.1 și 1 secunde
    return "Request processed"

# Endpoint pentru a apela procesul
@app.route("/")
def hello():
    process_request()
    return "Hello, World!"

if __name__ == "__main__":
    # Pornim serverul HTTP pe portul 8000
    start_http_server(8000)  # Acesta este portul pe care Prometheus va "scrape"-ui metricile
    app.run(host="0.0.0.0", port=5000)  # Aplicația va rula pe portul 5000

