""" BizBot Application """
import time
from biz.board import Board
from biz.config import write, compare
from biz.topic import prepare, dump
from biz.apis.api import deleted, get_threads, iterate

def biz_app() -> None:
    """docs"""
    board: Board = Board.initialize()
    new_ids: list = []
    prev_ids: list = []
    while True:
        time.sleep(15)
        threads = get_threads(board=board)
        # we shouldn't update the storage.txt until we compare.
        new_ids = prepare(threads)

        diff: list = compare(new_ids, prev_ids)
        prev_ids = new_ids
        deleted_ids: list = deleted(diff)
        if(len(deleted_ids) > 0):
            iterate(deleted_ids)
        # here we should update storage.txt with the new threads
        # clean and dump
        write("")
        dump(threads)
        new_ids = []
    
