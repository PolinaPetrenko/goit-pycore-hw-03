import re

def normalize_phone(phone_number):
    sanitized = re.sub(r'[^\d+]', '', phone_number.strip())
    if sanitized.startswith('+'):
        if not sanitized.startswith('+38'):
            pass
    elif sanitized.startswith('380'):
        sanitized = '+' + sanitized
    else:
        sanitized = '+38' + sanitized
        
    return sanitized


raw_numbers = ["    +38(050)123-32-34", "0503451234", "(050)8889900"]
sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print(sanitized_numbers)