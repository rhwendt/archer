#!/usr/bin/python
import getpass
import string
import subprocess
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

    # set the hostname
    hostname = input("Enter hostname for new system: ")
    print()
    # set the domain
    domain = input("Enter the domain for new system: ")
    print()
    # set the timezone
    result = subprocess.run(['tzselect'], stdout=subprocess.PIPE)
    timezone = result.stdout.decode('utf-8')
    print()

    # validate root password
    root_password = validate_password()

    # get new username for system
    username = input("Enter a username for new system: ")
    msg = f"Enter a password for '{username}': "
    user_password = validate_password(username, msg)

    # write non sensitive information
    with open('system.yml', 'a+') as file:
        file.write(f"username: {username}\n")
        file.write(f"hostname: {hostname}\n")
        file.write(f"domain: {domain}\n")
        file.write(f"timezone: {timezone}\n")

    # write sensitive information to a vault
    ansible_prefix = "ansible-vault encrypt_string -n"
    os.system(f"{ansible_prefix} root_password {root_password} >> system.yml")
    os.system(f"{ansible_prefix} user_password {user_password} >> system.yml")


if __name__ == '__main__':
    main()
