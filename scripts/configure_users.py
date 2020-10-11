#!/usr/bin/python
import getpass
import string
import random
import os


def generate_random_password(length: int = 20):
    letters = string.ascii_letters
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str


def validate_password(user: str = 'root',
                      msg: str = "Create root password for new system: "):
    while True:
        password = getpass.getpass(msg)
        confirm = getpass.getpass(f"Confirm password for '{user}': ")
        print()

        if password == confirm:
            return password
        else:
            print("*" * 25)
            print("Passwords did not match!")
            print("*" * 25)


def main():
    # add random password to .vaultpass
    with open('.vaultpass', 'w') as file:
        p = generate_random_password()
        file.write("'" + p + "'")

    # validate root password
    root_password = validate_password()

    # get new username for system
    username = input("Enter a username for new system: ")
    msg = f"Enter a password for '{username}': "
    password = validate_password(username, msg)

    # write ansible vault information
    ansible_prefix = "ansible-vault encrypt_string -n"
    os.system(f"{ansible_prefix} root_password {root_password} >> secret.yml")
    os.system(f"{ansible_prefix} username {username} >> secret.yml")
    os.system(f"{ansible_prefix} password {password} >> secret.yml")


if __name__ == '__main__':
    main()
