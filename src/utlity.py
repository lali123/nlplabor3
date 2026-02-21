import json
from datetime import datetime

def log_event(level: str, message: str, **kwargs):
    log_entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "level": level.upper(),
        "message": message,
        **kwargs
    }
    print(json.dumps(log_entry))
