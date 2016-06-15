#!/usr/local/bin/python
# -*- coding: utf-8 -*-

class Explosion():

    posX = 0
    posY = 0
    stage = [[]]
    stages = [[[]]]
    i = 0

    def __init__(self, posX, posY):
        stageOne = [["E"]]
        stageTwo = [["E","E","E"],["E"," ","E"],["E","E","E"]]
        stageThree = [[" ","E","E","E"," "],["E"," "," "," ","E"],["E"," "," "," ","E"],["E"," "," "," ","E"],[" ","E","E","E"," "]]
        stageFour = [[" "," ","E","E","E"," "," "],[" ","E"," "," "," ","E"," "],["E"," "," "," "," "," ","E"],["E"," "," "," "," "," ","E"],["E"," "," "," "," "," ","E"],[" ","E"," "," "," ","E"," "],[" "," ","E","E","E"," "," "]]
        stageFive = [[" "," ","E","E","E","E","E"," "," "],[" ","E","E"," "," "," ","E","E"," "],["E","E"," "," "," "," "," ","E","E"],["E"," "," "," "," "," "," "," ","E"],["E"," "," "," "," "," "," "," ","E"],["E"," "," "," "," "," "," "," ","E"],["E","E"," "," "," "," "," ","E","E"],[" ","E","E"," "," "," ","E","E"," "],[" "," ","E","E","E","E","E"," "," "]]
        self.stages.append(stageOne)
        self.stages.append(stageTwo)
        self.stages.append(stageThree)
        self.stages.append(stageFour)
        self.posX = posX
        self.posY = posY

    def paint(self, canvas, width, height):
        if(self.i>4):
            return True
        self.stage = self.stages[self.i]
        h = len(self.stage)
        w = len(self.stage[0])
        for y in range(h):
            for x in range(w):
                c = self.stage[y][x]
                if(c != " "):
                    Y = int(y+self.posY) - h/2
                    X = int(x+self.posX) - w/2
                    if(0<=Y and Y<height and 0<=X and X<width):
                        canvas[Y][X] = c
        self.i+=1
        return False
