#!/usr/local/bin/python
# -*- coding: utf-8 -*-
from MObject import MObject

class Bullet(MObject):

    def __init__(self, posX, posY):
        self.mObString = [["b"]]
        self.height    = 1
        self.width     = 1
        self.posX = posX
        self.posY = posY
        self.speedX = 0
        self.speedY = -4
