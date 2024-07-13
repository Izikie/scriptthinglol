import subprocess as sys
from utils import *

def update_system():
    """Update the system to the latest packages"""
    # TODO: Provides updateing for a variety of package managers/distributions

def disable_root():
    """Disable the root user account"""
    sys.run(["sudo", "passwd", "-l", "root"], check=True)
    print("Root account has been disabled")

def shadow_permissions():
    """Set shadow folder permission"""
    sys.run(["sudo", "chmod", "640", "/etc/shadow"], check=True)
    print("Shadow permissions have been set")
    
def password_policy():
    """Set password system policy"""
    # TODO: Implement password policy

def sudoers():
    """Check sudoers file for no authentication & set permissions"""
    # TODO: Implement sudoers no auth file check
    sys.run(["sudo", "chmod", "0440", "/etc/sudoers"], check=True)
    printSuccess("Sudoers permissions has been secured")

def network_configuration():
    """Configure networks settings for security"""
    # TODO: Implement

def system_all():
    update_system()
    disable_root()
    shadow_permissions()
    password_policy()
    sudoers()
    network_configuration()