from scripts.system import *
from scripts.program import *
from utils import *

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
        "name": "Sudoers File",
        "function": sudoers
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
        "name": "Service Cleanup",
        "function": service_cleanup
    },
    5: {
        "name": "All",
        "function": program_all
    }
}

def print_header():
    printFailed("THIS IS ENTERLY UNTESTED AT THE MOMENT. DO NOT USE\n")
    # TODO: Add a fancy ascii art header
    print("1. System Options")
    print("2. Program Options")
    print("3. Exit")

while True:
    print_header()
    category = int_input("\nCategory:", 1 , 3)

    if category == 3:
        break

    selected = system_options if category == 1 else program_options

    print(f"\n{'-' * 30}\n")
    for key, value in selected.items():
        print(f"{key}. {value['name']}")

    script = int_input("\nScript:", 1, len(selected))

    if script in selected:
        selected[script]["function"]()

    print()