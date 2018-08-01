from threading import *
import time
from Utility import *


class BackgroundTask:
    def __init__(self, fps, callback):
        self.interval = Utility.fps_to_millis(fps)
        self.callback = callback
        thread = Thread(target=self.run, args=())
        thread.daemon = True
        thread.start()

    def run(self):
        while True:
            self.callback()
            time.sleep(self.interval)
