#!/usr/bin/env python
import sys
import termios
import contextlib
import threading
import Queue

chars = Queue.Queue()

class Input(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    @contextlib.contextmanager
    def raw_mode(self, file):
        old_attrs = termios.tcgetattr(file.fileno())
        new_attrs = old_attrs[:]
        new_attrs[3] = new_attrs[3] & ~(termios.ECHO | termios.ICANON)
        try:
            termios.tcsetattr(file.fileno(), termios.TCSADRAIN, new_attrs)
            yield
        finally:
            termios.tcsetattr(file.fileno(), termios.TCSADRAIN, old_attrs)


    def run(self):
        with self.raw_mode(sys.stdin):
            try:
                while True:
                    #global char
                    char = ord(sys.stdin.read(1))
                    chars.put(char)
                    if char == 113:
                        break;
            except (KeyboardInterrupt, EOFError):
                pass

    def getChars(self):
        global chars
        return chars
