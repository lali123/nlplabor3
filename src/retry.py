import time
import functools

def retry(retries: int = 3, delay: float = 1.0):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(retries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if i == retries - 1: raise
                    time.sleep(delay * (2 ** i)) # Exponential backoff
        return wrapper
    return decorator
