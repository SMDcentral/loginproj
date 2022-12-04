USER_DATA = ['user1', 'user2', 'user3']
PASS_DATA = ['pass1', 'pass2', 'pass3']

def login(id):
    while True:
        id = input("User ID #: ")
        if id.isdigit():
            id = int(id)
            if 0 < id <= 3:
                id = id - 1
                break
            else:
                print("enter valid ID #")
        else:
            print("enter valid ID #")
    while True:
        user = input("Username: ")
        if user == USER_DATA[int(id)]:
            break
        else:
            print("Incorrect username.")
    while True:
        password = input("Password: ")
        if password == PASS_DATA[int(id)]:
            print("access granted")
            break
        else:
            print("incorrect password")

login(id)
