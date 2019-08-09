import threading
import time
import os

class Clean(object):

    @staticmethod
    def remove(filename):
        time.sleep(5)
        os.remove(filename)

    @staticmethod
    def scheduleRemove(filename):
        t = threading.Thread(target=Clean.remove args=filename)
        t.start()