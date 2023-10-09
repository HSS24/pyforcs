name = input("Enter your name: ")
col = input("what is your fav color? ")
pet = input("what is your first pets name?: ")
mnam = input("what is your mothers maiden name?: ")
sch = input("what is your first schools name?: ")

# Create or open a file for writing
with open('hackme.txt', 'w') as file:
    # Write user information to the file
    file.write(f"Name: {name}\n")
    file.write(f"Color: {col}\n")
    file.write(f"Pet Name: {pet}\n")
    file.write(f"mother;s maiden name: {mnam}\n")
    file.write(f"School name: {sch}\n")


print("User information has been saved to 'hackme.txt'")