from login import *
from bookTicket import *
from queryTicket import *
from bookTicket import *
from time import sleep
import multiprocessing

def book1():
    '''
    根据坐席类别订票
    :return:
    '''
    client = Login()
    client.userLogin()
    bt = BookTicket()
    flag = True
    while flag:
        try:
            if bt.bookTickets('刘恒强', '2019-01-24', '北京','武汉', 'M'):
                break
        except:
            pass

def book2(name):
    '''
    根据坐席类别和车次订票
    :return:
    '''
    # client = Login()
    # client.userLogin()
    # sleep(60)
    bt = BookTicket()
    flag = True
    while flag:
        sleep(2)
        try:
            if bt.bookTickets(name, '2019-01-26', '北京','武汉', 'M', ['G507']):
                break
        except:
            pass


if __name__ == '__main__':
    client = Login()
    client.userLogin()
    book2('刘恒强')
    # book2('李四')
    # p1 = multiprocessing.Process(target=book2, args=('刘恒强',))
    # p2 = multiprocessing.Process(target=book2, args=('张琳乐',))
    #
    # p1.daemon = True
    # p2.daemon = True
    #
    # p1.start()
    # p2.start()
    #
    # p1.join()
    # p2.join()