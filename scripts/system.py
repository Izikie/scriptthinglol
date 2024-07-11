import subprocess

def update_system():
    """Update the system to the latest packages"""
    # TODO: Provides updateing for a variety of package managers/distributions

def disable_root():
    """Disable the root user account"""
    subprocess.run(["sudo", "passwd", "-l", "root"], check=True)

def shadow_permissions():
    """Set shadow folder permission"""
    subprocess.run(["sudo", "chmod", "640", "/etc/shadow"], check=True)

def password_policy():
    """Set password system policy"""
    # TODO: Implement password policy
    # TODO: Check sudoers for no authentication

def network_configuration():
    """Configure networks settings for security"""

def system_all():
    update_system()
    disable_root()
    shadow_permissions()
    password_policy()
    network_configuration()