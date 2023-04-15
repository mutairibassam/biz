"""docs"""
import re
from biz.config import append

class Topic:
    """ 
    Simple class to segergate core logic.

    Topic class requires 4 arguments to be instantiated
        - thread id
        - thread subject
        - thread image url
        - thread comment

    we are using `~` symbol to be act as a delimiter when we want to 
    differentiate between values.
    
    append function add each thread in app local storage. 
    file path = "./storage.txt"
    """

    def __init__(self, thread_id, subject, image_url, comment):
        thread = f'{thread_id}~{subject}~{image_url}~{comment}\n'
        append(thread)


def prepare(threads):
    """
    threads are all the threads that we receive from Board API to be stored
    locally for future reference.

    since comment are not clean we need to remove special characters including
    the new line character \n as this will make it very difficult to diff among
    threads.
    
    Now we diff among threads if there is a new line.
    """
    thread_ids = []
    for thread in threads:
        thread_id = thread.id
        thread_ids.append(thread_id)

        # topic = thread.topic
        # clean_comment = re.sub(r'[^a-zA-Z0-9\s]+', '', topic.text_comment).replace("\n", "").replace("~","")
        # clean_title = str(topic.subject).replace("~","")

        # Topic(thread_id, clean_title, topic.thumbnail_url, clean_comment)
    return thread_ids

def dump(threads):
    """
    threads are all the threads that we receive from Board API to be stored
    locally for future reference.

    since comment are not clean we need to remove special characters including
    the new line character \n as this will make it very difficult to diff among
    threads.
    
    Now we diff among threads if there is a new line.
    """
    for thread in threads:
        thread_id = thread.id

        topic = thread.topic
        clean_comment = re.sub(r'[^a-zA-Z0-9\s]+', '', topic.text_comment).replace("\n", "").replace("~","")
        clean_title = str(topic.subject).replace("~","")

        Topic(thread_id, clean_title, topic.thumbnail_url, clean_comment)
