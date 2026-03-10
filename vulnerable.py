import os

def get_user(user_id):
    query = f"SELECT * FROM users WHERE id = {user_id}"
    return query

def config():
    api_key = "sk_live_test_abc123"
    password = "admin123"
    return api_key
