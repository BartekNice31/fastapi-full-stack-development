class User:
    def __init__(self,login,email,password):
        self.login=login
        self.email=email
        self.password=password
    def __repr__(self):
        return f"User(login='{self.login}', email='{self.email}')"

Users=[
    User("bartek", "bartek@example.com", "Haslo123!"),
    User("anna", "anna@example.com", "Anna2025!"),
    User("marek", "marek@example.com", "Marek#456"),
    User("kasia", "kasia@example.com", "Kasia789!"),
    User("tomek", "tomek@example.com", "Tomek321$")
]