# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 13:09:01 2020

@author: viic_
"""

class Element:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Frog(Element):
    width = 20
    height = 20
    vertical_steep = 40
    horizontal_steep = 10
    def __init__(self, x, y, xw1, yw1, xw2):
        self.x = x
        self.y = y
        self.xw1 = xw1
        self.yw1 = yw1
        self.xw2 = xw2
        self.yw2 = self.y + self.height
        
    def draw(self, w):
        w.create_rectangle(self.x, self.y, self.x + self.height, self.y + self.width, fill="green")
        
    def topReached(self):
        if self.y <= self.yw1+self.yw1/4: return True
        return False
        
    def moveup(self):
        self.y -= self.vertical_steep
        if self.y < self.yw1+self.yw1/4: self.y = self.yw1+self.yw1/4
    
    def movedown(self):
        self.y += self.vertical_steep
        if self.y > self.yw2-self.height: self.y = self.yw2-self.height
    
    def moveright(self):
        self.x += self.horizontal_steep
        if self.x > self.xw2-self.width: self.x = self.xw2-self.width
    
    def moveleft(self):
        self.x -= self.horizontal_steep
        if self.x < self.xw1: self.x = self.xw1


class Vehicle(Element):
    def __init__(self, x, y, speed = 5): # speed = 5 if any value is passed
        super().__init__(x, y)
        self.speed = speed
        
    def draw(self, w):
        if self.speed > 0:
            w.create_rectangle(self.x, self.y, self.x - self.width, self.y + self.height, fill="#ccccff")
            w.create_rectangle(self.x - (self.width * 0.25), self.y, self.x - (self.width * 0.25), self.y + self.height)
        else:
            w.create_rectangle(self.x, self.y, self.x + self.width, self.y + self.height, fill="#ff9999")
            w.create_rectangle(self.x + self.width * 0.25, self.y, self.x + self.width * 0.25, self.y + self.height)
            
    def move(self):
        self.x = (self.x + self.speed) % 800
        
class Car(Vehicle):
    width = 60
    height = 30
    
class Lorry(Vehicle):
    width = 80
    height = 30
    
