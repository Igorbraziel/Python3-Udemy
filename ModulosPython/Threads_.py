from time import sleep
from threading import Thread

class MyThread(Thread):
    def __init__(self, text, time):
        self.text = text
        self.time = time
        super().__init__()
    
    def run(self):
        sleep(self.time)
        print(self.text)
        

t1 = MyThread('Thread 1', 6)
t1.start()

t2 = MyThread('Thread 2', 3)
t2.start()

t3 = MyThread('Thread 3', 1)
t3.start()