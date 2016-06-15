import msvcrt
import threading
import Queue

chars = Queue.Queue()

class Input(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        while True:
            global char
            char = ord(msvcrt.getch())
            chars.put(char)
            if char == 113:
                break;

    def getChars(self):
        global chars
        return chars
