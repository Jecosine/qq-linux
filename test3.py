import thread,time

class Echo:
    def __init__(self):
        self.value = 1

    def run(self):
        thread.start_new_thread(self.thread_1,())
        while 1:
            print self.value
            time.sleep(1)

    def thread_1(self):
        self.value = 2

