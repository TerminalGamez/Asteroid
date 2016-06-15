#!/usr/local/bin/python
# -*- coding: utf-8 -*-
from MObject import MObject
from AstroidClass import AstroidClass

class Ship(MObject):

    def __init__(self, posX, posY):
        self.mObString = [[' ','S',' ',],['S','S','S',]]
        self.height    = 2
        self.width     = 3
        self.posX = posX
        self.posY = posY
        self.speedX = 0
        self.speedY = 0
