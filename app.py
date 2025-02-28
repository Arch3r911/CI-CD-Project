from flask import Flask, Response
from prometheus_client import start_http_server, Summary, generate_latest, CONTENT_TYPE_LATEST
import random
import time

app = Flask(__name__)

REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')

@app.route("/metrics")
def metrics():
    return Response(generate_latest(), content_type=CONTENT_TYPE_LATEST)  # Setăm corect Content-Type

@REQUEST_TIME.time()
def process_request():
    time.sleep(random.uniform(0.1, 1.0))
    return "Request processed"

@app.route("/")
def hello():
    process_request()
    return "Hello, World!"

if __name__ == "__main__":
    start_http_server(8000)
    app.run(host="0.0.0.0", port=5000)
