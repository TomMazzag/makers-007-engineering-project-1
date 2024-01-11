from lib.user import User


class UserRepository:
    def __init__(self, connection):
        self.connection = connection

    def all(self):
        users = []
        rows = self.connection.execute("SELECT * FROM users")

        for row in rows:
            user = User(row["id"], row["username"], row["email"], "None")
            users.append(user)
        return users

    def create(self, user):
        print("------------------------------------------")
        print(user)
        self.connection.execute(
            "INSERT INTO users (username, email, hashed_password) VALUES (%s, %s, %s)",
            [user.username, user.email, user.hashed_password],
        )

    def login_user(self, username, password):
        return False
