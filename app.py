from flask import Flask, Response
from prometheus_client import generate_latest, CONTENT_TYPE_LATEST, Summary
import random
import time

# Creăm aplicația Flask
app = Flask(__name__)

# Definim o metrică pentru timpul de execuție al unei funcții
REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')

# Endpoint pentru a expune metricile Prometheus
@app.route("/metrics")
def metrics():
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)  # ✅ Fix: Setăm tipul de conținut corect

# Funcție pentru a simula un proces de lungă durată
@REQUEST_TIME.time()  # Această decoratoare va măsura timpul de execuție
def process_request():
    time.sleep(random.uniform(0.1, 1.0))  # Întârziere aleatorie între 0.1 și 1 secunde
    return "Request processed"

# Endpoint pentru a apela procesul
@app.route("/")
def hello():
    process_request()
    return "Hello, World!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)  # ✅ Rulează pe portul 5000 pentru a se potrivi cu Prometheus
