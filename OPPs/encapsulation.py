class SecureAccount:
    def __init__(self, username, password):
        self.username = username
        self.__password = password  
    def get_password(self):
        return self.__password

    def set_password(self, new_password):
       
        if len(new_password) >= 8: 
            self.__password = new_password
            print("Password updated successfully.")
        else:
            print("Error: Password must be at least 8 characters long.")

    def get_username(self):
        return self.username


def main():

    account = SecureAccount("Soni Rathore", "12345678")
    print(f"Username: {account.get_username()}")
    print(f"Current Password: {account.get_password()}")
    account.set_password("123456690")
    account.set_password("123453467")
    print(f"Updated Password: {account.get_password()}")


if __name__=="__main__":
    main()
