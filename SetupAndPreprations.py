import pygame as game
import random
import numpy
import ClassesFile
import FunctionsFile as funct
#--------------------
game.init()
Width = 800
Height = 800
Canvas = game.display.set_mode((Width, Height))
game.display.set_caption("Canvas")
Switch = True
Clock = game.time.Clock()
FPS = 144 #FPS here
DraggingPoint = None
point = ClassesFile.POINT([Width/2, Height/2], Canvas)
point.color = "white"
walls = []
for i in range(5):
    walls.append(ClassesFile.BOUNDARY(random.randint(0, Width), random.randint(0, Height), random.randint(0, Width), random.randint(0, Height), "grey", Canvas))
#--------------------
while Switch:
    events = game.event.get()
    for event in events:
        if event.type == game.QUIT:
            Switch = False

    #Main code here...
    Canvas.fill("black")
    funct.Dragger(point, events, DraggingPoint)
    point.UpdateRays()
    point.CheckWall(walls, "red")
    for wall in walls:
        wall.Draw()
    point.Draw()


    game.display.update()
    Clock.tick(FPS)