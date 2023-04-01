import basc_py4chan

class Board():
    """
    Represents a 4chan board.

    Attributes:
        name (str): Name of this board, such as ``tg`` or ``k``.
        name (string): Name of the board, such as "tg" or "etc".
        title (string): Board title, such as "Animu and Mango".
        is_worksafe (bool): Whether this board is worksafe.
        page_count (int): How many pages this board has.
        threads_per_page (int): How many threads there are on each page.
    """
    __instance = None
    
    def __new__(self):
        """
        create a new Board object with Singleton pattern
        """
        if self.__instance is None:
            self.__instance = basc_py4chan.Board("yaz")
        return self.__instance

    @staticmethod 
    def initialize():
        """
        initialize new Board object with specific board name
        in our case we want to initialize Business & Finance (biz)
        
        other board examples [biz, o, p, v, vg, vm, vmg]
        """
        board: Board = Board()
        board.__init__("biz")
        return board 