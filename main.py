from scripts.system import *
from scripts.program import *

system_options = {
    1: {
        "name": "Update System",
        "function": update_system
    },
    2: {
        "name": "Disable Root User",
        "function": disable_root
    },
    3: {
        "name": "Shadow Permissions",
        "function": shadow_permissions
    },
    4: {
        "name": "Password Policy",
        "function": password_policy
    },
    5: {
        "name": "Network Configuration",
        "function": network_configuration
    },
    6: {
        "name": "All",
        "function": system_all
    }
}
program_options = {
    1: {
        "name": "Secure SSH",
        "function": secure_ssh
    },
    2: {
        "name": "Firewall",
        "function": firewall
    },
    3: {
        "name": "File Scan",
        "function": file_scan
    },
    4: {
        "name": "All",
        "function": program_all
    }
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
    print("\t1. System Options")
    print("\t2. Program Options")
    print("\t3. Exit")

    category_choice = int_input("Enter your choice:")

    if category_choice == 3:
        break

    options = system_options if category_choice == 1 else program_options

    if options is None:
        print("> Invalid category")
        continue

    print("Select an option:")
    for key, value in options.items():
        print(f"\t{key}. {value['name']}")

    option_choice = int_input("Enter your choice:")

    if option_choice in options:
        options[option_choice]["function"]()
    else:
        print("> Invalid choice")
    print()