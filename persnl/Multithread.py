import time
from threading import Thread
import threading
def dow(name):
    for i in range(5):
        time.sleep(1)
        print("hello frands",i,name)
class abc(Thread):
    def __init__(self,fname):
        super().__init__()
        self.fname=fname
    def run(self):
        dow(self.fname)
w1=abc("Ok Frands")
# time.sleep(1)
w2=abc("BBye")
w1.start()
time.sleep(1)
w2.start()
