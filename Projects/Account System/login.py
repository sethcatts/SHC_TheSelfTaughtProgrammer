userNameList = []
passwordList = []

def logInPrompt():
    username = input("Username: ")
    if(validUsername(username)):
        print("Valid")
    password = input("Password: ")
    if(validPassword(password))
        print("Valid")
        print("Login complete")

class user():
    def __init__(self, u, p):
        self.username = u
        self.password = p
    def user_exists(u):
        return u = self.username

    def change_password():
        currentPassword = input("Current password: ")
        if(currentPassword = self.password):
            newPassword = input("New Password: ")
            self.password = newPassword
        else:
            print("Wrong password")

admin = user("Admin", "password")

logInPrompt();
