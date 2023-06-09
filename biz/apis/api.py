"""docs"""
import requests as r
from requests.exceptions import HTTPError
from biz.board import Board
from biz.config import get_secret, read

token, chat_id = get_secret()

def send(
        thread_id: str,
        subject: str,
        thread_comment: str
    ) -> None:

    """
    Send function will be called everytime we need to send missing thread to 
    the telegram group. Send expects 4 different argumnts
    thread id:          thread id
    subject:            thread subject
    image_url:          thread image url [removed]
    thread_comment:     thread text comment 

    return              None

    /// archiver refers to a website that archives all 4chan threads and posts
    /// 
    /// [website url]       (https://archived.moe/)
    /// [biz board]         (https://archived.moe/biz)
    /// [specific thread]   (https://archived.moe/biz/thread/{thread_id})
    
    /// message just concatenates and formats thread details prior sending to 
    /// the telegram group.
    /// [output]
            Missing id: 54472365
            Subject: getting sued
            Archiver: https://archived.moe/biz/thread/54472365
            http://i.4cdn.org/biz/1680681193997391s.jpg [removed]
            v1.1

    /// telegram_url requires 1 url path and 2 query params
    /// 
    /// [token]     secert key that refer to your bot, you can get it from BotFather
    /// [chat_id]   chat id that you want to send to (can be group or private)
    /// [message]   the details that you want to send.
    /// [version]   app version 

    /// To send the data you just need to do simple GET request

    """
    archiver: str = f'https://archived.moe/biz/thread/{thread_id}'

    message: str = f"Missing id: {thread_id}\nSubject: {subject}\nComment: {thread_comment}\nArchiver: {archiver}\nv1.1"
    try:
        telegram_url: str = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}'
        r.get(telegram_url,timeout=5)
    except HTTPError as err:
        print(err)

def deleted(ids: list) -> list:
    """
    check if a specific id is deleted or archived using below url
    https://boards.4channel.org/biz/thread/{thread_id}

    if thread has been deleted the response status code will be 404

    if it's been deleted, it will be stored in `deleted_ids` list to be returned

    [note]
        list comprehension logic is commented because we don't use list comprehension for 
        readability purposes and since the array size will always be the same length 
        we compromise code readability over performance.

        ```snippet
        deleted_ids: list = [i for i in ids if r.get(url + str(i), timeout=5).status_code == 404]
        ```
    """
    url: str = 'https://boards.4channel.org/biz/thread/'

    not_found_ids: list = []
    for i in ids:
        try:
            response = r.get(url + str(i), timeout=10)
            if response.status_code == 404:
                not_found_ids.append(i)
        except HTTPError as err:
            print(err)
            continue
    return not_found_ids

def get_threads(board: Board) -> list:
    """ return all threads with its data """
    try:
        threads: list = board.get_all_threads()
        return threads
    except HTTPError as err:
        print(err)

def iterate(deleted_ids: list) -> None:
    """
    deleted_ids  ->  confirmed deleted ids

    iterate first read from what has been stored locally from ./storage.txt file
    by calling read(). Then the logic will iterate over all the stored lines.

    Each line will be unpacked to 4 values using `~` delimiter
        - thread id
        - thread subject
        - thread image url [removed]
        - thread comment

    if the thread id exist in thread deleted ids list, this means this is our target
    thread that we actually need to send to the telegram group by using send() 
    function.

    """
    local_data = read()
    for eachline in local_data:
        try:
            # _ variable is thread image url but it's been removed
            # since it might have inappropriate images
            thread_id, subject, _, *comment = eachline.split("~")
            if int(thread_id) in deleted_ids:
                print(f'thread to be sent: {thread_id}')
                send(thread_id, subject, comment)
        except ValueError as err:
            print(err)
            continue
        