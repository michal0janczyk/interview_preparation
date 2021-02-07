import threading

lock = threading.RLock()

lock.acquire()
lock.acquire()

print "Hello"

lock.release()
