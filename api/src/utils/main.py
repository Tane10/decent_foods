'''
limit =>  default 10 max 100
offset => query data and only get from X number i.e. select * from table offset=1o
page => size of the list i.e. 10, 25 , 50 etc
'''

MAX_PAGESIZE = 50


def pagination(items, offset=0, page_size=10):
    if page_size > MAX_PAGESIZE:
        page_size = MAX_PAGESIZE
