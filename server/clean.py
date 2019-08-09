import threading
import time
import os

class Clean(object):

    @staticmethod
    def remove(filename):
        time.sleep(10)
        try:
            os.remove(filename)
        except: pass
        finally: return

    @staticmethod
    def scheduleRemove(filename):
        t = threading.Thread(target=Clean.remove, args=[filename])
        t.start()