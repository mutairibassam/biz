
from Board import Board
    
def init():
    biz = Board()
    print(biz)
    print(biz.name)
    print(biz.title)
    print(biz.is_worksafe)
    print(biz.page_count)
    print(biz.threads_per_page)
 
if __name__ == '__main__':
    init()