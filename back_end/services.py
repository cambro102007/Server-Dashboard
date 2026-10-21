import subprocess

services = {
    "jellyfin": "jellyfin",
    "pihole": "pihole-FTL",
    "qbittorrent": "qbittorrent-nox",
    "nginx": "nginx"
}

def get_server_status(server):
    res = subprocess.run(
        ["systemctl", "is-active", server],
        capture_output=True,
        text=True
    )
    return res.stdout.strip() == "active"

def get_all_services():
    return {
        "jellyfin": get_server_status("jellyfin"),
        "pihole": get_server_status("pihole-FTL"),
        "qbittorrent": get_server_status("qbittorrent-nox"),
        "nginx": get_server_status("nginx"),
    }
