#!/usr/local/bin/python
# -*- coding: utf-8 -*-
from MObject import MObject
from Ship import Ship
from AstroidClass import AstroidClass
from Explosion import Explosion

class Collision():

    def collision(self, mObjects, explosions):
        for mOb1 in mObjects:
            for mOb2 in mObjects:
                #Ship
                if(isinstance(mOb1, Ship)):
                    #Ship, Astroid
                    if(isinstance(mOb2, AstroidClass)):
                        pos = self.collide(mOb1, mOb2)
                        if(pos!=None):
                            explosions.append(Explosion(pos[0],pos[1]))
        return None

    def collide(self, mOb1, mOb2):
        y = 0
        while(y < mOb1.height):
            x = 0
            while(x < mOb1.width):
                Y = y + int(mOb1.posY - mOb2.posY)
                X = x + int(mOb1.posX - mOb2.posX)
                if(0<=Y and Y<mOb2.height and 0<=X and X<mOb2.width):
                    if(mOb2.mObString[Y][X] != " " and mOb1.mObString[y][x] != " "):
                        return (x+mOb1.posX, y+mOb1.posY)
                x+=1
            y+=1
        return None