print("WELCOME TO THE LOGIN SYSTEM")
username = input("Enter your username: ")
password = input("Enter your password: ")
if username == "admin" and password == "password123":
    print("Login successful! Welcome, admin.")
else:
    print("Login failed! Invalid username or password.")