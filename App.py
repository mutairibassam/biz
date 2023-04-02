import requests as req
from board import Board
import time
    
def compare(new: list, prev: list) -> list:
    """
    current: the first list which will be the origianl source of the ids.
    new: the second list which will be compared against to get missing ids.

    difference: the finalized ids after getting the difference between
                original and prev lists.

    """
    if len(prev) == 0: return []
    difference: set = set(prev) - set(new)
    return list(difference)

def boardApp() -> None:
    board: Board = Board()
    new_ids: list = []
    prev_ids: list = []
    while True:
        try:
            new_ids: list = board.get_all_thread_ids()  
        except Exception as e:
            # todo: direct hit to https://a.4cdn.org/biz/threads.json
            # raise HTTPError("Sorry, Http error occured!")
            print(f'error {e}')
            continue 
        
        diff: list = compare(new_ids, prev_ids)
        prev_ids = new_ids
        # we need to check every thread id if it's deleted or archived
        result: list = isDeleted(diff)
        print(f'missing ids: {result}')
        time.sleep(10)

def isDeleted(result: list) -> list:
    deleted: list = []
    url: str = 'https://boards.4channel.org/biz/thread/'
    for i in result:
        res = req.get(url + str(i))
        if(res.status_code == 404):
            deleted.append(i)
    return deleted

if __name__ == '__main__':
    Board.initialize()
    boardApp()