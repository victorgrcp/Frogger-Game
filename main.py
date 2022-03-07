# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 12:07:53 2020

@author: Victor Garcia Pina
"""

import tkinter as tk
import keyboard
from time import sleep
from element import Frog
from lane import rightLane, leftLane

"""
##### FROGGER GAME #####

- USE 'WASD' TO MOVE
"""

WIDTH = 800
HEIGHT = 400
LANE_HEIGHT = 40
bestScore = 0
initialScore = 100
score = initialScore
initialLifes = 3
lifes = initialLifes
speedVehicles = 2
numberVehicles = 4
timeBetweenKeys = 0.1
pause = False

master = tk.Tk()
master.title("Frogger - Victor Garcia - Advanced Programming, Summer School '20 - UAB")
window = tk.Canvas(master, width = WIDTH, height = HEIGHT)
window.pack()

lanes = []
for i in range(3):
    l1 = rightLane(0, 80 + 2*LANE_HEIGHT*i, WIDTH, LANE_HEIGHT, i%2, numberVehicles, speedVehicles)
    l1.initCars()
    lanes.append( l1 )
    l2 = leftLane(0, 120 + 2*LANE_HEIGHT*i, WIDTH, LANE_HEIGHT, i%2, numberVehicles, speedVehicles)
    l2.initCars()
    lanes.append( l2 )
    
frog = Frog((WIDTH/2)-10, lanes[-1].y + LANE_HEIGHT + LANE_HEIGHT/4, 0, 40, WIDTH)

def updateBestScore(score, bestScore):
    if bestScore < score: return score
    return bestScore

def startPositionFrog():
    frog.x = (WIDTH/2)-10
    frog.y = lanes[-1].y + LANE_HEIGHT + LANE_HEIGHT/4
    
while True:
    
    if not pause:
        if timeBetweenKeys >= 0.1:
            if  keyboard.is_pressed("w"): frog.moveup()
            elif keyboard.is_pressed("a"): frog.moveleft()
            elif keyboard.is_pressed("d"): frog.moveright()
            elif keyboard.is_pressed("s"): frog.movedown()
            timeBetweenKeys = 0
        
    if keyboard.is_pressed("p"):
        pause = not pause
        timeBetweenKeys = 0
        
    window.delete("all")
    
    window.create_rectangle(0, 0, WIDTH, 40, fill="#d4831f")
    window.create_rectangle(0, HEIGHT-40, WIDTH, HEIGHT, fill="#d4831f")
    
    for lane in lanes:
        lane.draw(window)
        lane.drawCars(window)
    
    frog.draw(window)
    
    if pause:
        window.create_rectangle(340, 180, 460, 220, fill="#fbc777")
        window.create_text(WIDTH/2, HEIGHT/2, font=("Purisa", 16),
        text="PAUSED")
    else:
        for lane in lanes:
            lane.moveCars()
        
        if frog.topReached():
            window.create_rectangle(300, 140, 500, 240, fill="#fbc777")
            window.create_text(WIDTH/2, HEIGHT/2 -30, font=("Purisa", 14),
            text="YOU WIN !!")
            window.create_text(WIDTH/2, HEIGHT/2, font=("Purisa", 14),
            text=f"FINAL SCORE:")
            window.create_text(WIDTH/2, HEIGHT/2 + 20, font=("Purisa", 14),
            text= str(round(score, 2)) )
            window.update()
            
            bestScore = updateBestScore(score, bestScore)
            startPositionFrog()
            score = initialScore
            lifes = initialLifes
            sleep(3)
        
        for lane in lanes:
            if lane.collision(frog):
                lifes -= 1
                window.create_rectangle(280, 180, 520, 220, fill="#fbc777")
                window.create_text(WIDTH/2, HEIGHT/2, font=("Purisa", 14),
                text="A vehicle run over the frog!!")
                window.update()
                sleep(2)
                if lifes == 0:
                    window.create_rectangle(280, 180, 520, 220, fill="#fbc777")
                    window.create_text(WIDTH/2, HEIGHT/2, font=("Purisa", 18),
                    text="GAME OVER !!")
                    window.update()
                    sleep(3)
                    lifes = initialLifes
                    score = initialScore
                startPositionFrog()
        
        if score <= 0:
            window.create_rectangle(340, 180, 460, 220, fill="#fbc777")
            window.create_text(WIDTH/2, HEIGHT/2, font=("Purisa", 14), 
                               text= "TIME OUT !!" )
            window.update()
            sleep(3)
            score = initialScore
            lifes = initialLifes
            startPositionFrog()
        
        score -= 0.05
    
    window.create_text(WIDTH/2, 20, font=("Purisa", 16), 
                       text="FINISH!")
    window.create_text(WIDTH/2, HEIGHT-20, font=("Purisa", 16), 
                       text="START!")
    window.create_text(WIDTH-120, HEIGHT-20, font=("Purisa", 10), 
                       text="*Press 'p' to pause the game")
    window.create_text(60, 20, font=("Purisa", 12),
                       text= f"LIFES: {lifes}")
    window.create_text(160, 20, anchor=tk.W, font=("Purisa", 12),
                       text= f"SCORE: {round(score, 1)}")
    window.create_text(WIDTH - 180, 20, anchor=tk.W, font=("Purisa", 12),
                       text= f"BEST SCORE: {round(bestScore, 2)}")
    window.update()
    timeBetweenKeys += 0.05
    sleep(0.05)
    
    

