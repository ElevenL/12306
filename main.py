from login import *
from bookTicket import *
from queryTicket import *
from bookTicket import *
from time import sleep
import datetime
import multiprocessing

def book(names, date, fromStation, toStation, seatType, trainNames):
    '''
    根据坐席类别和车次订票
    :return:
    '''
    bt = BookTicket()
    flag = True
    while flag:
        sleep(1)
        try:
            if bt.bookTickets(names, date, fromStation, toStation, seatType, trainNames):
                break
        except Exception as e:
            print(e)
            pass

if __name__ == '__main__':
    client = Login()
    client.userLogin()
    date = (datetime.datetime.now()+datetime.timedelta(days=29)).strftime("%Y-%m-%d")
    book(['刘恒强'], '2019-02-02', '北京', '武汉', 'O', ['G83', 'G81', 'G79', 'G421', 'G405', 'G487', 'G401','G507', 'G485', 'G529',
                                                  'G71', 'G403', 'G309', 'G511', 'G65', 'G487'])
    # book(['刘恒强', '张琳乐'], '2019-01-27', '武汉', '白沙铺', 'O', ['D3245', 'D3289'])
    # book2('李四')
    # p1 = multiprocessing.Process(target=book, args=('刘恒强',))
    # p2 = multiprocessing.Process(target=book, args=('张琳乐',))
    #
    # p1.daemon = True
    # p2.daemon = True
    #
    # p1.start()
    # p2.start()
    #
    # p1.join()
    # p2.join()