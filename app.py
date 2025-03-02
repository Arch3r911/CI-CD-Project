from flask import Flask, jsonify, request
from prometheus_client import start_http_server, Summary, Counter
import time

app = Flask(__name__)

#Prometheus
REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')
USER_CREATED = Counter('user_created_total', 'Number of users created')

@REQUEST_TIME.time()
@app.route('/create_user', methods=['POST'])
def create_user():
    data = request.get_json()
    time.sleep(0.5)  
    USER_CREATED.inc()
    return jsonify({"message": f"User {data['name']} created successfully!"})

@REQUEST_TIME.time()
@app.route('/metrics')
def metrics():
    from prometheus_client import generate_latest
    return generate_latest()

if __name__ == '__main__':
    start_http_server(8000)
    app.run(host='0.0.0.0', port=5000) 
