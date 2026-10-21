import psutil
import time
import subprocess

# This function retrieves the current CPU usage percentage of the Raspberry Pi.
def get_cpu_usage():
    cpu_usage = psutil.cpu_percent(interval=1)
    
    return cpu_usage

def get_memory_usage():
    memory = psutil.virtual_memory()
    return memory.percent

def get_storage_usage():
    storage = psutil.disk_usage('/mnt/media')
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
    res = subprocess.run(
        ["vcgencmd", "measure_temp"],
        capture_output=True,
        text=True
    )
    return float(res.stdout.strip().replace("temp=", "").replace("'C", ""))