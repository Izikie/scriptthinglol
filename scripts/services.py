from utils import *

def secure_ssh():
    # Backup OpenSSH config
    run(["cp", "/etc/ssh/sshd_config", "/etc/ssh/sshd_config.bak"])
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
        run(["sed", "-i", f"s/^#*{settings} .*/{settings} {value}/", "/etc/ssh/sshd_config"])

    run(["systemctl", "restart", "ssh"])

    print_success("SSH service has been secured")