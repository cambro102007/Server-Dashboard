import psutil
import time

# This function retrieves the current CPU usage percentage of the Raspberry Pi.
def get_cpu_usage():
    cpu_usage = psutil.cpu_percent(interval=1)
    
    return cpu_usage

def get_memory_usage():
    memory = psutil.virtual_memory()
    return memory.percent

def get_storage_usage():
    storage = psutil.disk_usage('/')
    return round(storage.total / (1024 ** 3), 2)

def get_uptime():
    boot_time = psutil.boot_time()
    uptime_seconds = time.time() - boot_time
    uptime_hours = uptime_seconds / 3600
    return round(uptime_hours, 2)
