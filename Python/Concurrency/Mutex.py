from threading import Lock
from threading import Thread

def processData(data):
    mutex = Lock()
    mutex.acquire()

    try:
        print('Do some stuff')
        return
        # exception may be thrown here
    finally:
        print "release"
        mutex.release()

def main():
    print "start"

    t = Thread(target = processData, args = (1,))
    t.start()

if __name__ == "__main__":
    main()
