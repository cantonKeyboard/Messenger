def create_account():
    global username
    global password
    username = str(input("Enter your username- "))
    password = str(input("Enter your password- "))
    confirm = str(input("Enter your password again- "))
    if confirm == password:
        print("Confirmed!")
    else:
        print("Error. Please try again.")

def message():
    confirm_username = str(input("Please enter your username- "))
    confirm_password = str(input("Please enter your password- "))
    if confirm_username == username:
        if confirm_password == password:
            reciever = str(input("Person to message- "))
            message = str(input("Message here- "))
            print(username, "sent to", reciever, " --> ", message)
        else:
            print("Please type info() to check your username and password.")
    else:
        print("Please type info() to check your username and password.")

def info():
    print("Username =",username)
    print("Password = ",password)
