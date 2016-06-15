#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import random

from AstroidClass import AstroidClass

class AstroidSpawner():

    width = 0
    height = 0
    i = 0

    def __init__(self, width, height):
        self.width = width
        self.height = height


    def spawnAstroid(self, astroids):
        if (random.randint(1,1000) + self.i > 990):
            self.i=0
            astroidStr = self.randomAstroidStr()
            astroidPosX = random.randint(3-len(astroidStr[0]),self.width - 3 + len(astroidStr[0]))
            astroidPosY = 2 - len(astroidStr)
            astroidSpeedX = 0
            astroidSpeedY = random.random()+.1
            astroid = AstroidClass(astroidStr, astroidPosX, astroidPosY, astroidSpeedX, astroidSpeedY)
            astroids.append(astroid)
        else:
            self.i+=1

    def randomAstroidStr(self):
        return [["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"]]
