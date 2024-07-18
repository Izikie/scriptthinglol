import subprocess as sys
from utils import *

def update_system():
    """Update the system to the latest packages"""
    # TODO: Provides updateing for a variety of package managers/distributions
    run(["apt", "update", "-y"])
    run(["apt", "upgrade", "-y"])

def disable_root():
    """Disable the root user account"""
    run(["passwd", "-l", "root"])
    printSuccess("Root account has been disabled")

def shadow_permissions():
    """Set shadow folder permission"""
    run(["chmod", "640", "/etc/shadow"])
    printSuccess("Shadow permissions have been set")
    
def password_policy():
    """Set password system policy"""
    # TODO: Implement

def sudoers():
    """Check sudoers file for no authentication & set permissions"""
    result = run(["grep", "NOPASSWD\\|!authenticate", "/etc/sudoers"])

    if result.returncode == 0:
        printWarning("Insecure sudoers file found (NOPASSWD or !authenticate)")
        # TODO: Implement fix

    printSuccess("Sudoers file is secure")

    run(["chmod", "0440", "/etc/sudoers"])
    printSuccess("Sudoers permissions has been set")

def system_all():
    update_system()
    disable_root()
    shadow_permissions()
    password_policy()
    sudoers()