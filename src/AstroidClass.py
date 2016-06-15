#!/usr/local/bin/python
# -*- coding: utf-8 -*-
from MObject import MObject

class AstroidClass(MObject):

    def __init__(self, initMObString, posX, posY, speedX, speedY):
        self.mObString = initMObString
        self.height    = len(initMObString)
        self.width     = len(initMObString[0])
        self.posX = posX
        self.posY = posY
        self.speedX = speedX
        self.speedY = speedY
