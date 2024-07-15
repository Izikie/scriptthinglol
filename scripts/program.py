import subprocess as sys

def secure_ssh():
    """Configure OpenSSH with more secure settings"""

    installPackage("openssh-server")
    
    # Backup OpenSSH config
    run(["cp", "/etc/ssh/sshd_config", "/etc/ssh/sshd_config.bak"])
    printSuccess("Config backup has been created (/etc/ssh/sshd_config.bak)")

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
    """Configure firewall (UFW) with secure settings"""
    installPackage("ufw")

    run(["ufw", "enable"])
    printSuccess("Firewall has been enabled")

    run(["ufw", "logging", "on"])
    printSuccess("Firewall logging has been enabled")

    # TODO: Sysctl settings
    printSuccess("Firewall has been secured")

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