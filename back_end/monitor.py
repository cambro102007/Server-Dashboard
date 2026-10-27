import psutil
import time
import subprocess
import platform

# This function retrieves the current CPU usage percentage of the Raspberry Pi.
def get_cpu_usage():
    cpu_usage = psutil.cpu_percent(interval=1)
    
    return cpu_usage

def get_memory_usage():
    memory = psutil.virtual_memory()
    return memory.percent

def get_storage_usage():
    storage = psutil.disk_usage('/')
    return {
        "total": round(storage.total / (1024 ** 3), 2),
        "used": round(storage.used / (1024 ** 3), 2),
        "free": round(storage.free / (1024 ** 3), 2),
        "percent": storage.percent
    }

def get_uptime():
    boot_time = psutil.boot_time()
    uptime_seconds = time.time() - boot_time
    uptime_hours = uptime_seconds / 3600
    return round(uptime_hours, 2)

def get_temp():
    if platform.system() == "Darwin":
        return None
    # Runs a command in the Raspberry pi terminal then returns the output
    res = subprocess.run(
        ["vcgencmd", "measure_temp"],
        capture_output=True,
        text=True
    )
    return float(res.stdout.strip().replace("temp=", "").replace("'C", ""))

def get_network_usage():
    first_network = psutil.net_io_counters()
    time.sleep(1)
    second_network = psutil.net_io_counters()

    #comparing two network usages a second later to get /s and divides to make is mb's
    upload = (second_network.bytes_sent - first_network.bytes_sent) / 1000000
    download = (second_network.bytes_recv - first_network.bytes_recv) / 1000000

    return {
        "upload": round(upload, 3),
        "download": round(download, 3)
    }