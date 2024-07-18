import subprocess as sys

def int_input(message, min=None, max=None):
    while True:
        try:
            value = int(input(message + ' '))

            if (min is not None and value < min) or (max is not None and value > max):
                print(f"Please enter a number between {min} and {max}.")
            else:
                return value
        except ValueError:
            printFailed("Invalid input. Please enter a valid number.")

def prompt_input(message):
    while True:
        value = input(message + ' (y/n) ').lower()

        if value in ['y', 'n', 'yes', 'no']:
            return value == 'y' or value == "yes"
        printFailed("Invalid input. Please enter a valid value.")

def printSuccess(message):
    print(f"\033[92m{message}\033[00m")

def printWarning(message):
    print(f"\033[33m{message}\033[00m")

def printFailed(message):
    print(f"\033[91m{message}\033[00m")

# TODO: add proper error handling
def run(cmd, error=True, output=False):
    try:
        return sys.run(["sudo", *cmd], check=error, capture_output=output)
    except sys.CalledProcessError as e:
        printFailed(f"Failed to run command: {' '.join(cmd)}")
        printFailed(f"Error: {e}")
        exit(1)

def installPackage(package):
    if run(["dpkg", "-l", "|", "grep", "-q", package], output=True).returncode != 0:
        printWarning(f"Installing {package}...")
        # TODO: Support multiple package managers
        run(["apt", "install", package, "-yq"])
        printSuccess(f"{package} has been installed")
    else:
        printWarning(f"{package} is already installed")