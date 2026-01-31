users = {
    "admin": "1234",
    "student": "resume123"
}

def login(username, password):
    return users.get(username) == password
