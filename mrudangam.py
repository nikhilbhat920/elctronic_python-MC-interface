import time
import threading
import winsound
from funcs_for_play import *
'''
format of serial data:

1 33.32/n2 32/n3 20.32

1 33.32
2 32
3 20.32


'''


t1= threading.Thread(target=check_n_play_S1)
t2= threading.Thread(target=check_n_play_S2)
t3= threading.Thread(target=check_n_play_S3)

while(True):
    t1.start()
    t2.start()
    t3.start()
    #t1.join()
    #t2.join()
    #t3.join()
