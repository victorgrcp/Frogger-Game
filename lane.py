# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 12:42:05 2020

@author: viic_
"""

from element import Car, Lorry
from random import randint, seed


class Lane:
    def __init__(self, x, y, width, height, typeVehicle, numCars, carSpeed):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.typeVehicle = typeVehicle  # 0 (Car), 1 (lorry)
        self.numCars = numCars
        self.carSpeed = carSpeed
        self.cars = []
    
    def initCars(self):
        seed()
        if self.typeVehicle == 0:
            for i in range(self.numCars):
                self.cars.append( Car(self.x + randint(2, 6)*10+ +i*140, self.y+5, self.carSpeed) )
        else:
            for i in range(self.numCars):
                self.cars.append( Lorry(self.x + self.width - randint(1, 6)*10 - i*160, self.y+5, self.carSpeed) )
        
    def draw(self, w):
        w.create_rectangle(self.x, self.y, self.x+self.width, self.y+self.height,
                           fill="#858175")
        w.create_line(self.x, self.y, self.x+self.width, self.y,
                      dash=(8, 4), fill="white")
        w.create_line(self.x, self.y+self.height, self.x+self.width, self.y+self.height,
                      dash=(8, 4), fill="white")
        
    def drawCars(self, w):
        for car in self.cars:
            car.draw(w)
            
    def moveCars(self):
        for car in self.cars:
            car.move()
            
            
class leftLane(Lane):
    def __init__(self, x, y, width, height, typeVehicle,numCars, carSpeed):
        super().__init__(x, y, width, height, typeVehicle, numCars, carSpeed)
        self.carSpeed = -carSpeed

    def collision(self, frog):
        for car in self.cars:
            if (car.y < frog.y < (car.y + car.height)):
                if ((car.x <= frog.x <= (car.x + car.width))) or (car.x <= (frog.x + frog.width) <= (car.x + car.width)):
                    return True
        return False

class rightLane(Lane):
    def collision(self, frog):
        for car in self.cars:
            if (car.y < frog.y < (car.y + car.height)):
                if ((car.x >= frog.x >= (car.x - car.width))) or (car.x >= (frog.x + frog.width) >= (car.x - car.width)):
                    return True
        return False
    
    