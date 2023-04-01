
from board import Board
import time
    
def compare(orginal: list, prev: list) -> list:
    difference: set = set(orginal) - set(prev)
    return list(difference)

def check():
    board: Board = Board()
    original_ids: list = []
    prev_ids: list = []
    while True:
        original_ids: list = board.get_all_thread_ids()
        if len(prev_ids) == 0:
            prev_ids = original_ids
            continue 
        result: list = compare(original_ids, prev_ids)
        print("removed ids " + result)
        time.sleep(10)
    
if __name__ == '__main__':
    Board.initialize()
    check()