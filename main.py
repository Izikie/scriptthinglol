from scripts.system import *
from scripts.program import *
from utils import *

system_options = {
    1: {
        "name": "Users",
        "function": update
    },
    2: {
        "name": "Passwords",
        "function": passwords
    },
    3: {
        "name": "Update",
        "function": update
    },
    4: {
        "name": "Disable Root User",
        "function": disable_root
    },
    5: {
        "name": "Shadow Permissions",
        "function": shadow_permissions
    },
    6: {
        "name": "Sudoers File",
        "function": sudoers
    }
}
program_options = {
    1: {
        "name": "File Scan",
        "function": file_scan
    },
    2: {
        "name": "Services",
        "function": services
    },
    3: {
        "name": "Unwanted",
        "function": unwanted
    },
    5: {
        "name": "Firewall",
        "function": firewall
    }
}

def print_header():
    # TODO: Add a fancy ascii art header
    print_success('#' * 45)
    print_success("""\n    _/_/_/    _/                               
   _/    _/  _/    _/_/      _/_/    _/_/_/    
  _/_/_/    _/  _/_/_/_/  _/_/_/_/  _/    _/   
 _/    _/  _/  _/        _/        _/    _/    
_/_/_/    _/    _/_/_/    _/_/_/  _/_/_/       
                                 _/            
                                _/
""")
    print_failed("THIS IS ENTERLY UNTESTED AT THE MOMENT. DO NOT USE\n")
    print_success('#' * 45)
    print("1. System Options")
    print("2. Program Options")
    print("3. Exit")

while True:
    print_header()
    category = int_input("\nCategory:", 1 , 3)

    if category == 3:
        break

    selected = system_options if category == 1 else program_options

    print_success(f"\n{'#' * 30}\n")
    for key, value in selected.items():
        print(f"{key}. {value['name']}")

    script = int_input("\nScript:", 1, len(selected))

    if script in selected:
        selected[script]["function"]()

    print()