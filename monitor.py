import psutil
import time
from datetime import datetime

CPU_THRESHOLD = 80
MEMORY_THRESHOLD = 80
DISK_THRESHOLD = 90

def check_alerts(cpu, memory, disk):
    alerts = []
    
    if cpu > CPU_THRESHOLD:
        alerts.append(f"⚠️ HIGH CPU USAGE: {cpu}%")
    
    if memory > MEMORY_THRESHOLD:
        alerts.append(f"⚠️ HIGH MEMORY USAGE: {memory}%")
    
    if disk > DISK_THRESHOLD:
        alerts.append(f"⚠️ HIGH DISK USAGE: {disk}%")
    
    return alerts

with open('system_monitor.log', 'a', encoding='utf-8') as log_file:
    while True:
        cpu = psutil.cpu_percent(interval=1)
        memory = psutil.virtual_memory().percent
        disk = psutil.disk_usage('/').percent
        
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        alerts = check_alerts(cpu, memory, disk)
        
        log_line = f"{timestamp} | CPU: {cpu}% | Memory: {memory}% | Disk: {disk}%"
        
        if alerts:
            log_line += f" | ALERTS: {', '.join(alerts)}"
        
        log_line += "\n"
        log_file.write(log_line)
        print(log_line.strip())
        
        time.sleep(5)