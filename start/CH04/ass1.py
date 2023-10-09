name = input("Enter your name: ")
age = input("Enter your age: ")
email = input("Enter your email address: ")

# Create or open a file for writing
with open('user_info.txt', 'w') as file:
    # Write user information to the file
    file.write(f"Name: {name}\n")
    file.write(f"Age: {age}\n")
    file.write(f"Email: {email}\n")

print("User information has been saved to 'user_info.txt'")