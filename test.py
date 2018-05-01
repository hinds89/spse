# Code from https://stackoverflow.com/questions/18348991/python-threading-stdin-stdout
# accessed 7:45 PM 19/04/2018
import threading
import time

class parser(threading.Thread):
    def __init__ (self, data_input):
        threading.Thread.__init__(self)
        self.data_input = data_input

    def run(self):
        for elem in self.data_input:
            time.sleep(3)
            with self.output_lock:
	         print elem + 'Finished'

work = ['a', 'b', 'c', 'd', 'e', 'f']

thread1 = parser(['a', 'b'])  
thread2 = parser(['c', 'd'])
thread3 = parser(['e', 'f'])

thread1.start()
thread2.start()
thread3.start()
