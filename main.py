from login import *
from bookTicket import *
from queryTicket import *
from bookTicket import *

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

def book2():
    '''
    根据坐席类别和车次订票
    :return:
    '''
    client = Login()
    client.userLogin()
    bt = BookTicket()
    flag = True
    while flag:
        try:
            if bt.bookTickets('刘恒强', '2019-01-23', '北京','武汉', 'M', ['G485']):
                break
        except:
            pass


if __name__ == '__main__':
    book2()