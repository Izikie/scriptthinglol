import subprocess as sys
from utils import sudo, install_package, print_success, print_warning

def update():
    install_package("unattended-upgrades")

    sudo(["systemctl", "start", "unattended-upgrades", "-yq"])

    sudo(["apt", "update", "-y"])
    sudo(["apt", "upgrade", "-y"])

def disable_root():
    sudo(["passwd", "-l", "root"])
    print_success("Root account has been disabled")

def shadow_permissions():
    sudo(["chmod", "640", "/etc/shadow"])
    print_success("Shadow permissions have been set")
    
def passwords():
    """Set password & policy"""

def sudoers():
    result = sudo(["grep", "NOPASSWD\\|!authenticate", "/etc/sudoers"])

    if result.returncode == 0:
        print_warning("Insecure sudoers file found (NOPASSWD or !authenticate)")
        input("Press any key to continue...")
    else:
        print_success("Sudoers file is secure")

    sudo(["chmod", "0440", "/etc/sudoers"])
    print_success("Sudoers permissions has been set")