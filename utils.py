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

def printSuccess(message):
    print(f"\033[92m{message}\033[00m")

def printWarning(message):
    print(f"\033[33m{message}\033[00m")

def printFailed(message):
    print(f"\033[91m{message}\033[00m")