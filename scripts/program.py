import subprocess as sys
from utils import *

def secure_ssh():
    """Configure OpenSSH with more secure settings"""

    installPackage("openssh-server")
    
    # Backup OpenSSH config
    run(["cp", "/etc/ssh/sshd_config", "/etc/ssh/sshd_config.bak"])
    printWarning("Config backup has been created (/etc/ssh/sshd_config.bak)")

    settings = { # TODO: Add more settings
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

    printSuccess("OpenSSH has been configured")
    printSuccess("Restarting SSH service")
    run(["systemctl", "restart", "ssh"])
    printSuccess("SSH service has been secured")

def firewall():
    """Configure firewalL/sysctl network settings"""
    installPackage("ufw")

    run(["ufw", "enable"])
    printSuccess("Firewall has been enabled")

    run(["ufw", "logging", "on"])
    printSuccess("Firewall logging has been enabled")

    while True:
        port = int_input("Enter a port (0 to continue)", 0, 65535) or 0
        if port == 0:
            break

        run(["ufw", "allow", str(port)])

    while True:
        service = input("Enter a service (0 to continue) ") or '0'
        if service == "0":
            break

        run(["ufw", "allow", service])

    while True:
        ip = input("Enter an IP address (0 to continue) ") or '0'
        if ip == "0":
            break

        run(["ufw", "allow", f"from {ip}"])

    # Sysctl settings
    run(["cp", "/etc/sysctl.conf", "/etc/sysctl.bak"])
    printWarning("Config backup has been created (/etc/sysctl.conf.bak)")

    settings = {
        "net.ipv4.conf.default.rp_filter": "1",
        "net.ipv4.conf.all.rp_filter": "1",

        "net.ipv4.conf.all.accept_redirects": "0",
        "net.ipv4.conf.all.send_redirects": "0",
        "net.ipv4.conf.all.accept_source_route": "0",
        "net.ipv4.conf.all.log_martians": "1",
        "net.ipv4.ip_forward": "0",
        "net.ipv4.tcp_syncookies": "1",
        "net.ipv6.conf.all.disable_ipv6": "1",
    }

    for setting, value in settings.items():
        run(["sed", "-i", f"s/^#*{settings} .*/{settings}={value}/", "/etc/sysctl.conf"])

    run(["sysctl", "-p"])

    printSuccess("Firewall/Network has been secured")

# TODO: Scan extentions from a configuration file
file_extensions = [
    # Video/
	"mp4", "mpeg", "avi", "mpg", "webm", "mov",
	# Pictures
	"png", "jpg", "jpeg", "gif", "bmp", "tiff", "raw",
	# Audio
	"mp3", "ogg", "m4a", "wav", "flac",
	# Misc
	"txt", "docx", "pdf", "doc", "ppt", "pptx", "xls", "ps"
]

# No Idea If This Works
def file_scan():
    """Scans the file system for files with specific extensions"""
    files = 0
    for ext in file_extensions:
        result = run(["find", "/", "-name", f"*.{ext}"], output=True)
        if result:
            # TODO: Save the result to a file
            files += 1            
        printSuccess(f"Found {files} files with extension {ext}")

services = ["ftp", "ssh", "telnet", "nginx"] # TODO: Add more services

def service_cleanup():
    """Disable unnecessary exploitable services"""
    for service in services:
        if prompt_input(f"Would you like to disable {service}?"):
            run(["systemctl", "disable", service])
            run(["systemctl", "stop", service])
            printSuccess(f"{service} has been disabled and stopped") 

def program_all():
    secure_ssh()
    firewall()
    file_scan()
    service_cleanup()