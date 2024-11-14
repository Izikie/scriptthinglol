import subprocess as sys
from utils import sudo, print_warning, print_success

def secure_ssh():
    # Backup OpenSSH config
    sudo(["cp", "/etc/ssh/sshd_config", "/etc/ssh/sshd_config.bak"])
    print_warning("Config backup has been created (/etc/ssh/sshd_config.bak)")

    settings = {
        "PermitRootLogin": "no",
        "PasswordAuthentication": "no",
        "PermitEmptyPasswords": "no",
        "UsePAM": "yes",
        "UserPrivilegeSeparation": "yes",
        "LoginGraceTime": "60",

        "Protocol": "2",
        "X11Forwarding": "no",
    }

    for settings, value in settings.items():
        sudo(["sed", "-i", f"s/^#*{settings} .*/{settings} {value}/", "/etc/ssh/sshd_config"])

    sudo(["systemctl", "restart", "ssh"])

    print_success("SSH service has been secured")