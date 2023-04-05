from board import Board
import time
import re
from apis.api import send, deleted
from config import append, write
    
def compare(new: list, prev: list) -> list:
    """
    @current: the first list which will be the origianl source of the ids.
    @new: the second list which will be compared against to get missing ids.

    @difference: the finalized ids after getting the difference between
                original and prev lists.

    """
    if len(prev) == 0: return []
    difference: set = set(prev) - set(new)
    return list(difference)

def boardApp() -> None:
    board: Board = Board.initialize()
    new_ids: list = []
    prev_ids: list = []
    while True:
        time.sleep(10)
        write(" ")
        try:
            o: list = board.get_all_threads()
            # new_ids: list = board.get_all_thread_ids()
        except Exception as e:
            # e -> to be logged
            print(e)
            continue 
        

        # we need to store subject, thumbnail, and id
        for i,_ in enumerate(o):
            cmt = re.sub(r'[^a-zA-Z0-9\s]+', '', o[i].topic.text_comment).replace("\n", "")
            Topic(
                o[i].id,
                o[i].topic.subject,
                o[i].topic.thumbnail_url,
                cmt
            )
            new_ids.append(o[i].id)
        

        # we need to know all missing ids
        diff: list = compare(new_ids, prev_ids)
        prev_ids = new_ids
        result: list = deleted(diff)
        print(result)
        # # we need to extract missing ids metadata from local storage
        with open('./storage.txt', 'r') as file:
            for line in file:
                id,sub,img,comment = line.split("~")
                if int(id) in result:
                    print(f'Missing id: {id}\nSubject: {sub}\n{img}\n{comment}')
        # we need to send id metadata to telegram group
                    send(id, sub, img, comment)
        new_ids = []

class Topic:
    def __init__(self, thread_id, subject, image_url, comment):
        thread = f'{thread_id}~{subject}~{image_url}~{comment}\n'
        append(thread)


if __name__ == '__main__':
    boardApp()
