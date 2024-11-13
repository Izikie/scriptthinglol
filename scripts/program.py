from utils import *
from services import *

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
    files = 0
    for ext in file_extensions:
        result = run(["find", "/", "-name", f"*.{ext}"], output=True)
        if result:
            # TODO: Save the result to a file
            files += 1
        print_success(f"Found {files} files with extension {ext}")

packages = {
    "unwanted": ["wireshark", "ophcrack", "john", "hydra"],
    "services": ["ftp", "openssh-server", "x2goserver", "telnet", "nginx", "apache2", "snmp", "vpn"],
    "bloat": ["gnome-games", "transmission", "deluge"]
}

def unwanted():
    print_warning("Removing malware/hack tools")
    for package in packages["unwanted"]:
        run(["apt", "purge", f"*{package}*"])

    print_warning("Removeing bloat")
    for package in packages["bloat"]:
        run(["apt", "purge", f"*{package}*"])

def services():
    for service in packages["services"]:
        if bool_input(f"Do you want {service}?"):
            install_package(service)

            if service == "openssh-server":
                secure_ssh()

            run(["systemctl", "enable", service])
            print_success(f"{service} has been installed")
        else:
            run(["apt", "purge", f"*{service}*"])
            print_warning(f"{service} has been uninstalled")

def firewall():
    install_package("ufw")

    run(["ufw", "enable"])
    run(["ufw", "logging", "on"])

    print_success("UFW has been configured")

    # Sysctl settings
    run(["cp", "/etc/sysctl.conf", "/etc/sysctl.bak"])
    print_warning("Config backup has been created (/etc/sysctl.conf.bak)")

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

    print_success("Systemctl network settings have been configured")