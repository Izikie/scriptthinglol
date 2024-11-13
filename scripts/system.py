from utils import *

def update():
    install_package("unattended-upgrades")

    run(["systemctl", "start", "unattended-upgrades", "-yq"])

    run(["apt", "update", "-y"])
    run(["apt", "upgrade", "-y"])

def disable_root():
    run(["passwd", "-l", "root"])
    print_success("Root account has been disabled")

def shadow_permissions():
    run(["chmod", "640", "/etc/shadow"])
    print_success("Shadow permissions have been set")
    
def passwords():
    """Set password & policy"""

def sudoers():
    result = run(["grep", "NOPASSWD\\|!authenticate", "/etc/sudoers"])

    if result.returncode == 0:
        print_warning("Insecure sudoers file found (NOPASSWD or !authenticate)")
        input("Press any key to continue...")
    else:
        print_success("Sudoers file is secure")

    run(["chmod", "0440", "/etc/sudoers"])
    print_success("Sudoers permissions has been set")