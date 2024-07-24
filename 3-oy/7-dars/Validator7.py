class UserValidator:
    def __init__(self, username: str, password: str, name: str, surname: str):
        assert isinstance(username, str) and len(username) >= 8, "Invalid username"
        assert isinstance(password, str) and len(password) >= 5, "Invalid password"
        assert isinstance(name, str), "Invalid name"
        assert isinstance(surname, str), "Invalid surname"
