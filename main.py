from scripts.system import *
from scripts.program import *

options = {
    1: {
        "name": "Disable Root User",
        "function": disable_root
    },
    2: {
        "name": "Secure SSH",
        "function": secure_ssh
    },
    3: {
        "name": "Password Policy",
        "function": password_policy
    },
    4: {
        "name": "Firewall",
        "function": firewall
    },
    5: {
        "name": "Update System",
        "function": update_system
    },
    6: {
        "name": "Network Configuration",
        "function": network_configuration
    },
    7: {
        "name": "Shadow Permissions",
        "function": shadow_permissions
    },
    8: {
        "name": "File Scan",
        "function": file_scan
    },
}

def int_input(message, min=None, max=None):
    while True:
        try:
            value = int(input(message + ' '))
            if (min is not None and value < min) or (max is not None and value > max):
                print(f"Please enter a number between {min} and {max}.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")

while True:
    print("Select an option:")

    print("\t0. Exit")
    for key, value in options.items():
        print(f"\t{key}. {value['name']}")

    choice = int_input("Enter your choice:")

    if choice == 0:
        break

    if choice in options:
        options[choice]["function"]()
    else:
        print("> Invalid choice")
    print()