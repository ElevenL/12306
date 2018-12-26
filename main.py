from login import *
from bookTicket import *
from queryTicket import *
from bookTicket import *

client = Login()
client.userLogin()
bt = BookTicket()
bt.bookTickets('刘恒强', '2019-01-24', '北京','武汉', 'M')