import subprocess as sys
from utils import *

def secure_ssh():
    """Configure OpenSSH with more secure settings"""

def firewall():
    """Configure firewall (UFW) with secure settings"""

# TODO: Scan extentions from a configuration file
file_extensions = [
    # Video
	"mp4" "mpeg" "avi" "mpg" "webm" "mov" "wav"
	# Pictures
	"png" "jpg" "jpeg" "gif" "bmp" "tiff" "raw"
	# Audio
	"mp3" "ogg" "m4a" "flac"
	# Misc
	"txt" "docx" "pdf" "doc" "ppt" "pptx" "xls" "ps"
]

files_found = 0
def file_scan():
    """Scans the file system for files with specific extensions"""
    files_found = 0

services = ["ftp", "ssh", "telnet", "nginx"] # TODO: Add more services

def service_cleanup():
    """Disable unnecessary exploitable services"""
    for service in services:
        # TODO: add y/n prompt handling
        if input(f"Would you like to disable {service}? (y/n) ").lower() == "y":
            sys.run(["sudo", "systemctl", "disable", service], check=True)
            sys.run(["sudo", "systemctl", "stop", service], check=True)
        printSuccess(f"{service} has been disabled and stopped") 

def program_all():
    secure_ssh()
    firewall()
    file_scan()
    service_cleanup()