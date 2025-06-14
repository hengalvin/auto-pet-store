import json
import os

def load_json(file_name):
    file_path = os.path.join(os.path.dirname(__file__), file_name)
    with open(file_path) as f:
        return json.load(f)
    
def log_response(response):
    print(f"\n[Request] {response.request.method} {response.request.url}")
    print(f"[Payload] {response.request.body}")
    print(f"[Response] {response.status_code} {response.text}")


