import psutil

def check_process_running(process_name: str):
    for proc in psutil.process_iter(['name']):
        if process_name.lower() in proc.info['name'].lower():
            return True
    return False

# Usage: print(f"Is Resolve running? {check_process_running('Logmein')}")
