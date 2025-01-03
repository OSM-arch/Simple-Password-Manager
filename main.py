import hashlib
from random import choice

name_pass_list = []

def display():
    print("Welcome To your Password Manager: ")
    print("1. Add Password\n"
          "2. Remove Password\n"
          "3. Update Password\n"
          "4. Show all my Passwords\n"
          "5. Exit"
          )

def show():
    for i in name_pass_list:
        print(f"App: {i[0]} | Password: {i[1]}")

def add():
    print("Enter 'q' to exit: ")

    while True:
        name = input("Password for: ").lower()

        if name == 'q':
            break

        if any(name == entry[0] for entry in name_pass_list):
            print("This name already exists. Please enter a different name.")
            continue

        try:
            if not name.isascii():
                raise ValueError("Invalid input! Please enter alphabetic characters only.")

            password = input("Password: ")
            if not password.strip():
                raise ValueError("Invalid input! Password cannot be empty.")

            name_pass_list.append([name, password])

        except ValueError as e:
            print(e)
            continue

def Remove():
    print("Enter 'q' to exit and 'all' to delete everything: ")
    show()

    while True:
        del_name = input("Which one you want to delete: ")

        if del_name == 'q':
            break

        if del_name == 'all':
            name_pass_list.clear()
            print("Everything is removed successfully")
            break

        for i in name_pass_list:

            for j in i:

                if del_name == j:
                    name_pass_list.remove(i)
                    print(f"{del_name} is successfully removed")
                    show()
                else:
                    break

def update():
    print("Enter 'q' to exit: ")

    while True:

        show()
        update_choice = input("Enter the exact name to change: ").lower()

        if update_choice == 'q':
            break

        print("1. Update Name\n"
              "2. Update Password"
              )
        try:
            choice = int(input("Choose: "))
        except:
            print("Invalid input!")
            continue

        for i in name_pass_list:
            if i[0] != update_choice:
                print("Name not found!")

            elif i[0] == update_choice:
                print(i)
                if choice == 1:
                    i[0] = input("Enter a New Name :").lower()
                    break

                elif choice == 2:
                    i[1] = input("Enter a New Password :").lower()
                    break


# Function to hash the master password
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def verify_master_password():
    stored_master_password_hash = hash_password("oussama") # Replace with your actual master password
    while True:
        master_password = input("Enter master password: ")
        if hash_password(master_password) == stored_master_password_hash:
            print("Access granted.")
            break
        else:
            print("Invalid master password. Try again.")

verify_master_password()
# Call the function
while True:
    display()
    choice = int(input("Choose: "))
    match choice:
        case 1: add()
        case 2: Remove()
        case 3: update()
        case 4: show()
        case 5: quit()