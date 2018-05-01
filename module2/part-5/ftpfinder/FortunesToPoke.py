#!/usr/bin/env python

import Queue
import threading
import ftplib
import os

from ftplib import FTP

# color class found in stackoverflow. Seems good enough for this task, and
#it is cross platform
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'



class WorkerThread(threading.Thread):

    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue

    def run(self):
        global count
        global ftp
        count = 0

        print bcolors.OKGREEN + "FTP Thread, born to be alive" + bcolors.ENDC
        while count is not 10:
            # get queue, and handle emptyness
            #
            try:
                w = queue.get(timeout = 0.3)
            except Queue.Empty:
                break
            try:
                #remove CRLF from line
                w = w.rstrip('\n\r')
                ftp = FTP(w)
                ftp.login()
                print bcolors.OKGREEN + "\n {} contain the following folders:\n".format(w) + bcolors.ENDC
                ftp.dir()
                count +=1
            except Exception, e:
                print bcolors.FAIL + "\nConnection to {} not possible due to the following error: {}".format(w,str(e))+ bcolors.ENDC
                pass
        ftp.quit()
        self.queue.task_done()
        print bcolors.OKBLUE +"\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"
        print                   "$ 10 FTP servers scanned... $"
        print                   "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n"+ bcolors.ENDC
        os._exit(0) # sys.exit() exits thread only!




queue = Queue.Queue()



def main():
    try:
        for i in range(5):
            print bcolors.HEADER + "Creating workerThread : {}".format(i)+ bcolors.ENDC
            worker = WorkerThread(queue)
            worker.setDaemon(True)
            worker.start()
            print bcolors.OKBLUE + "WorkerThread {} created".format(i)+ bcolors.ENDC


        with open("f500.txt") as lines:
            line = lines.readlines() # readline until EOF is reached
            for l in line:
                queue.put(l)
            queue.join()
    except:
        pass

if __name__=="__main__":
    print bcolors.OKGREEN + "\n$$$$$$$$$$$$$$$$$$$$$$$$$$"
    print "$$$$ Fortunes To Poke $$$$ "
    print "$$$$$$$$$$$$$$$$$$$$$$$$$$\n"+ bcolors.ENDC
    main()

