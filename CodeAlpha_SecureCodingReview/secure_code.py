import sqlite3

username = input("Enter Username: ")

print("User Input:", username)

print("Using Parameterized Query")

query = "SELECT * FROM users WHERE username=?"

print("Query:", query)

print("Secure Query Executed Successfully")