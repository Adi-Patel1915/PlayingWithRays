import pygame as game
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
pointtest = ClassesFile.POINT([Width/2, Height/2], Canvas)
Boundrytest = ClassesFile.BOUNDARY(600, 100, 600, 700, Canvas)
#--------------------
while Switch:
    events = game.event.get()
    for event in events:
        if event.type == game.QUIT:
            Switch = False

    #Main code here...
    Canvas.fill("black")
    funct.Dragger(pointtest, events, DraggingPoint)
    pointtest.UpdateRays()
    pointtest.CheckWall(Boundrytest)
    pointtest.Draw()
    Boundrytest.Draw()


    game.display.update()
    Clock.tick(FPS)