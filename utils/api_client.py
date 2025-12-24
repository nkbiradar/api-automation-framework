import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def get_users():
    return requests.get(f"{BASE_URL}/users")

def get_user_by_id(user_id):
    return requests.get(f"{BASE_URL}/users/{user_id}")

def create_post(payload):
    return requests.post(f"{BASE_URL}/posts", json=payload)
