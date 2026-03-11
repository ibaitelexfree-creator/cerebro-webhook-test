def get_user(user_id):
    query = f"SELECT * FROM users WHERE id = {user_id}"
    password = "admin123"
    return query
def get_user_v2(user_id):
    query = f"SELECT * FROM users WHERE id = {user_id}"
    return query
