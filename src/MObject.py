#!/usr/local/bin/python
# -*- coding: utf-8 -*-

class MObject():

    mobString = [[]]
    width = 0
    heigth = 0
    posX = 0
    posY = 0
    speedX = 0
    speedY = 0

    def __init__(self, initMObString, posX, posY, speedX, speedY):
        self.mObString = initMObString
        self.height    = len(initMObString)
        self.width     = len(initMObString[0])
        self.posX = posX
        self.posY = posY
        self.speedX = speedX
        self.speedY = speedY

    def get(self):
        return mobString


    def move(self, width, height):
        self.posX+=self.speedX
        self.posY+=self.speedY
        Y = int(self.posY)
        X = int(self.posX)
        if(-self.height<=Y and Y<height+self.height and -self.width<=X and X<width+self.width):
            return False
        else:
            return True

    def paint(self, canvas, width, height):
        for y in range(self.height):
            for x in range(self.width):
                c = self.mObString[y][x]
                if(c != " "):
                    Y = int(y+self.posY)
                    X = int(x+self.posX)
                    if(0<=Y and Y<height and 0<=X and X<width):
                        canvas[Y][X] = c
