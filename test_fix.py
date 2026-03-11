def login(user):
    query = f"SELECT * FROM users WHERE id = {user}"
    api_key = "sk_live_test_abc"
    return query
