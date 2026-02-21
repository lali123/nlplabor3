import re

def mask_entities(text: str) -> str:
    # Basic masks for emails and IP addresses
    text = re.sub(r'\S+@\S+', '[EMAIL]', text)
    text = re.sub(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', '[IP_ADDR]', text)
    return text
