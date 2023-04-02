import requests as r
from config import get_secret

token, id = get_secret()
def send(message: str):
    try:
        full: str = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={id}&text={message}'
        r.get(full)
    except Exception as e:
        print(e)
