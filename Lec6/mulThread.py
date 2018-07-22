import time
from threading import Thread
import threading
def download(name):
    for i in range(5):
        time.sleep(1)#provide 1sec of timelap
        print("We have downloaded",i,name)
class Worker(Thread):
    def __init__(self,fname):
        super().__init__()
        self.fname=fname
    def run(self):
        download(self.fname)
w=Worker("Hello Frands")
w1=Worker("bbye frands")
w.start()
time.sleep(2)
w1.start()#w.run call one by one it takes time to download
for i in threading.enumerate():
    print(i.isAlive())#check t):
    if(i.name =="Helo Frands"he alive threads
for i in threading.enumerate():
        i.join()
# total thread
# print("Hello cb")
