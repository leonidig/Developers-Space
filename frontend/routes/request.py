import requests

class APIClient:
    def __init__(self, backend_url: str):
        self.backend_url = backend_url

    def send_request(self, method, endpoint: str, data: dict = None):
        url = f"{self.backend_url}/{endpoint}"
        response = method(url, json=data)
        return response
