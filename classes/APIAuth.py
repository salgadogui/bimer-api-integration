import requests
import os
from functools import wraps

class APIAuth:
    def __init__(self) -> None:
        self.api_base_url = os.environ["API_PRODUCTION_BASE_URL"]
        self.auth_url = os.environ["API_AUTH_URL"]
        self.client_id = os.environ["API_CLIENT_ID"]
        self.grant_type = os.environ["API_GRANT_TYPE"]
        self.username = os.environ["API_USERNAME"]
        self.password = os.environ["API_PASSWORD"]
        self.nonce = os.environ["API_NONCE"]
        self.access_token = None
        
    def ensure_authenticated(method):
        @wraps(method)
        def wrapper(self, *args, **kwargs):
            if not self.is_authenticated():
                self.authenticate()
            return method(self, *args, **kwargs)
        return wrapper

    def is_authenticated(self):
        return self.access_token is not None

    def authenticate(self):
        data = {
            "client_id": self.client_id,
            "grant_type": self.grant_type,
            "username": self.username,
            "nonce": self.nonce,
            "password": self.password
        }
        response = requests.post(self.auth_url, data=data)
        if response.status_code == 200:
            print("API authentication succeeded!")
            self.access_token = response.json().get('access_token')
        else:
            raise Exception(f"Authentication failed: {response.status_code}, {response.text}")
