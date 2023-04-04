import requests as r
from config import get_secret

token, chat_id = get_secret()
@DeprecationWarning
def send_deprecated(message: str):
    print(message)
    try:
        full: str = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}'
        res = r.get(full)
        print(res.status_code)
    except Exception as e:
        print(e)

def send(id, sub, img):
    archiver = f'https://archived.moe/biz/thread/{id}'
    message = f'Missing id: {id}\nSubject: {sub}\nArchiver: {archiver}\n{img}'
    try:
        full: str = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}'
        r.get(full, timeout=10)
    except Exception as e:
        print(e)

def deleted(ids: list) -> list:
    '''
    check if a specific id is deleted or archived using below url
    https://boards.4channel.org/biz/thread/{thread_id}

    if thread has been deleted the response status code will be 404

    if it's been deleted, it will be stored in `d` list to be returned

    '''
    d: list = []
    url: str = 'https://boards.4channel.org/biz/thread/'
    d = [i for i in ids if r.get(url + str(i)).status_code == 404]
    return d