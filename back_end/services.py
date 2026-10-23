import subprocess

services = {
    "jellyfin": "jellyfin",
    "pihole": "pihole-FTL",
    "qbittorrent": "qbittorrent-nox",
    "nginx": "nginx"
}

def get_server_status(server):
    return None

def get_all_services():
    return {
        "jellyfin": get_server_status("jellyfin"),
        "pihole": get_server_status("pihole-FTL"),
        "qbittorrent": get_server_status("qbittorrent-nox"),
        "nginx": get_server_status("nginx"),
    }
