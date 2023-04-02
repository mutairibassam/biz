import requests as req
from board import Board
import time
from apis.api import send
    
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


def deleted(ids: list) -> list:
    '''
    check if a specific id is deleted or archived using below url
    https://boards.4channel.org/biz/thread/{thread_id}

    if thread has been deleted the response status code will be 404

    if it's been deleted, it will be stored in `d` list to be returned

    '''
    d: list = []
    url: str = 'https://boards.4channel.org/biz/thread/'
    d = [i for i in ids if req.get(url + str(i)).status_code == 404]
    return d

def boardApp() -> None:
    board: Board = Board.initialize()
    new_ids: list = []
    prev_ids: list = []
    while True:
        try:
            new_ids: list = board.get_all_thread_ids()  
        except Exception as e:
            # e -> to be logged
            continue 
        
        diff: list = compare(new_ids, prev_ids)
        prev_ids = new_ids

        result: list = deleted(diff)
        if len(result) > 0: send(result)
        time.sleep(10)


if __name__ == '__main__':
    boardApp()