username = input("Enter Username: ")

query = "SELECT * FROM users WHERE username='" + username + "'"

print(query)