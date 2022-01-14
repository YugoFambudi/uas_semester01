import itertools
import threading
import time
import sys


class load:

    def loading(self):
        done = False

        def animated():
            for c in itertools.cycle(['|', '/', '-', '\\']):
                if done:
                    break
                sys.stdout.write('\rMemperoses data ' + c)
                sys.stdout.flush()
                time.sleep(0.1)

        t = threading.Thread(target=animated)
        t.start()

        time.sleep(3)
        done = True