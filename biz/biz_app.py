""" BizBot Application """
import time
from biz.board import Board
from biz.config import write, compare
from biz.topic import prepare
from biz.apis.api import deleted, get_threads, iterate

def biz_app() -> None:
    """docs"""
    board: Board = Board.initialize()
    new_ids: list = []
    prev_ids: list = []
    while True:
        setup()
        threads = get_threads(board=board)
        threads_id = prepare(threads)
        new_ids.append(threads_id)

        diff: list = compare(new_ids, prev_ids)
        prev_ids = new_ids
        deleted_ids: list = deleted(diff)
        iterate(deleted_ids)
        new_ids = []

def setup():
    """docs"""
    time.sleep(100)
    write(" ")
