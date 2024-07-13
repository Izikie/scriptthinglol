from utils import *

def secure_ssh():
    """Configure OpenSSH with more secure settings"""

def firewall():
    """Configure firewall (UFW) with secure settings"""
    # TODO: Add auto install + sysctl settings
    run(["ufw", "logging", "on"])
    printSuccess("Firewall logging has been enabled")

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

def file_scan():
    """Scans the file system for files with specific extensions"""
    for ext in file_extensions:
        # TODO: Add scan functionality
        printSuccess(f"Found {len(1)} files with extension {ext}")

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