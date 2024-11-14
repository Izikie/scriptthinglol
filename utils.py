import subprocess as sys

def int_input(message, min=None, max=None):
    while True:
        try:
            value = int(input(message + ' '))

            if (min is not None and value < min) or (max is not None and value > max):
                print_warning(f"Invalid Input, Enter a number from {min} to {max}.")
            else:
                return value
        except ValueError:
            print_warning("Invalid Input, Enter a valid integer number.")

def bool_input(message):
    while True:
        value = input(message + ' (y/n) ').lower()

        if value in ['y', 'yes', 'n', 'no']:
            return value == ['y', 'yes']
        print_warning("Invalid input. Please enter a valid value.")

def print_success(message):
    print(f"\033[92m{message}\033[00m")

def print_warning(message):
    print(f"\033[33m[!] {message}\033[00m")

def print_failed(message):
    print(f"\033[91m{message}\033[00m")

def sudo(cmd, error=True, output=False):
    try:
        return sys.run(["sudo", *cmd], check=error, capture_output=output)
    except sys.CalledProcessError as e:
        print_failed(f"Failed to run command: {' '.join(cmd)}")
        print_failed(f"Error: {e}")
        exit(1)

def install_package(package):
    if sudo(["dpkg", "-l", "|", "grep", "-q", package], output=True).returncode != 0:
        print_warning(f"Installing {package}...")
        sudo(["apt", "install", package, "-yq"])
        print_success(f"{package} has been installed")
    else:
        print_warning(f"{package} is already installed")