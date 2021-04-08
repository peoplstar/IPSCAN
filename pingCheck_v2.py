import threading
import os
import platform

threadLock = threading.Lock()
threads = []

print("Start Scan")
def isUp(hostname):
    if platform.system() == "Windows":
        threadLock.acquire()
        response = os.system("ping " + hostname + " -n 1")
        threadLock.release()
    else:
        threadLock.acquire()
        response = os.system("ping -c 1 " + hostname)
        threadLock.release()